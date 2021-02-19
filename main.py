#import psycopg2
#from config import config
import requests
import json
from sql_database import SQLDatabase



sql = """INSERT INTO vendors(vendor_name)
         VALUES(%s) RETURNING vendor_id;"""
#insert_vendor(sql)

data_link = 'https://8syg62n83a.execute-api.eu-north-1.amazonaws.com/dev/vd'

x = requests.get(data_link)
data = x.json()
print(data[0]['sector'])

#for x in data[0]['sector']:
    #print(x)

sector = "Offentlig"
amount = data[0]['sector']['Offentlig']
date = data[0]['date'][0:10]
location = data[0]['location']

print(sector, amount, date, location)

table = "public.sector"
columns = "sector, amount, date, location"
values = "'%s', %s, '%s', '%s'" %(sector, amount, date, location)

database = SQLDatabase()

database.insert_data(table, columns, values)

database.disconnect()





