from urllib.request import urlopen
from bs4 import BeautifulSoup
from collections import OrderedDict
import pyexcel
url = "http://s.cafef.vn/bao-cao-tai-chinh/VNM/IncSta/2017/3/0/0/ket-qua-hoat-dong-kinh-doanh-cong-ty-co-phan-sua-viet-nam.chn"
conn = urlopen(url)
raw_data = conn.read()
page_content = raw_data.decode("utf8")
with open("cafef.html","wb") as f:
    f.write(raw_data)
soup = BeautifulSoup(page_content,"html.parser")
header = soup.find("div",id="divTableHeader")
header_list = header.find_all("td")
table_header = []
for td in header_list:
    text = td.text.strip()
    table_header.append(text)

table = soup.find("table",id="tableContent")
table_data = []
rows = table.find_all("tr")
for row in rows:
    col_list = []
    cols = row.find_all("td")
    for col in cols[:5]:
        cell = col.text.strip()
        col_list.append(cell)
        data = OrderedDict(dict(zip(table_header,col_list)))
    table_data.append(data)
pyexcel.save_as(records=table_data, dest_file_name="cafef VNM.xlsx")