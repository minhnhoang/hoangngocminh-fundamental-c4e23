import pyexcel
from collections import OrderedDict #save date in order

#2 data prep
country_capitals = [
    OrderedDict({
        "Country": "Vietnam",
        "Capital": "Hanoi",
    }),
    OrderedDict({
        "Country": "China",
        "Capital": "Beijing",
    }),
    OrderedDict({
        "Country": "Thailand",
        "Capital": "Bangkok",
    })
]
# List comprehension

#3 save file using save_as()
pyexcel.save_as(records=country_capitals, dest_file_name="country capital.xlsx")