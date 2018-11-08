from urllib.request import urlopen
from bs4 import BeautifulSoup
from collections import OrderedDict
import pyexcel

#1. Connect to the page
url = "https://dantri.com.vn"
conn = urlopen(url)

#2. Download the page content
raw_data = conn.read()
page_content = raw_data.decode("utf8") #utf8: unicode type of text data
# print(page_content)
with open("dantri.html","wb") as f: #wb: write binary, to bypass Unicode error when save page_content
    f.write(raw_data)

#3. Find ROI (Region of Interest)
soup = BeautifulSoup(page_content, "html.parser")
#print(soup.prettify())
ul = soup.find("ul", "ul1 ulnew") # href="", id=""
#print(ul.prettify())
#4. Extract data
li_list = ul.find_all("li") # return a list of soups
news_list = []
for li in li_list:
    # li = li_list[0] # return a soup in list
    # h4 = li.h4
    # a = h4.a
    a = li.h4.a
    title = a.string #extract the content/string of tag
    link = url + a["href"] #extract attribute href (a dict)
    news =OrderedDict({
        "title": title,
        "link": link,
    })
    news_list.append(news)
#5. Save data
pyexcel.save_as(records=news_list, dest_file_name="dantri.xlsx")
