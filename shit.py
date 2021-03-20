import json
import csv
import pandas as pdz
import requests
import sqlite3
file = "data_file.json"
blog = {'PhoneTypeMdmid': 'datacamp.com', '<AaitionalProperties>': 'fff', "addressTypeMdmid": 89, 'fullAddress': '', 'countryCd': '',
        "zipCode": "", "regionType": "","region": "","areaType": "","area": "", "location": "","locationType": "", "locationType": "",
        "building": "","cityType": "","city": "","streetType": "","street": "","corp": "","house": "","apartment": "","kladr": "", "flasld": "",
        "<AdditionalProperties>": ""
        }


with open(file, "w") as write_file:
    json.dump(blog, write_file)

file = 'data_file.json'
with open(file,'r') as load_file:
    new_file = json.load(load_file)
    news = open('text1.json','w')
news.write('{' + '\n')
for i ,v  in new_file.items():
    c, j = i, type(v)
    j = str(j).strip("<class>")
    news.write( "'"+c+"'" + ' : ' + str(j) + ',' + '\n')

news.write('}' + '\n')
