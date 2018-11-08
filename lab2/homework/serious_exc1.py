from urllib.request import urlopen
from bs4 import BeautifulSoup
from collections import OrderedDict
from youtube_dl import YoutubeDL
import pyexcel
url = "https://www.apple.com/itunes/charts/songs/"
conn = urlopen(url)
raw_data = conn.read()
page_content = raw_data.decode("utf8")
with open("itune.html","wb") as f:
    f.write(raw_data)
soup = BeautifulSoup(page_content,"html.parser")
section = soup.find("section","section chart-grid")
ul = section.div.ul
li_list = ul.find_all("li")
song_list = []
options = {
    'default_search': 'ytsearch',
    'max_download': 1,
    'format': 'bestaudio/audio',
}
d1 = YoutubeDL(options)
for li in li_list:
    h3a = li.h3.a
    h4a = li.h4.a
    song_name = h3a.string
    artist = h4a.string
    song = OrderedDict({
        "song name": song_name,
        "artist": artist,
    })
    song_list.append(song)
    d1.download([song_name, artist])
pyexcel.save_as(records=song_list,dest_file_name="itune top chart.xlsx")


