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



database = SQLDatabase()

for date_and_location in data:
    for sector in date_and_location['sector']:
        amount = date_and_location['sector'][sector]
        date = date_and_location['date'][0:10]
        location = date_and_location['location']

        table = "public.sector"
        columns = "sector, amount, date, location"
        values = "'%s', %s, '%s', '%s'" %(sector, amount, date, location)

        database.insert_data(table, columns, values)

database.disconnect()





