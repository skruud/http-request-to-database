#import psycopg2
#from config import config
import requests
import json
from sql_database import SQLDatabase

#data_link = 'https://8syg62n83a.execute-api.eu-north-1.amazonaws.com/dev/vd'

#x = requests.get(data_link)
#data = x.json()

with open('olddata.json', 'r', encoding='utf-8-sig') as myfile:
    data=myfile.read()

data = json.loads(data)

database = SQLDatabase()

category = 'Alle yrker'

for row in data:
    amount = row['totalAds']
    date = row['date'][0:10]
    location = row['location']

    public_table = "public.%s" %('occupation')
    columns = "category, amount, date, location"
    values = "'%s', %s, '%s', '%s'" %(category, amount, date, location)
    print(values)
    database.insert_data(public_table, columns, values)

database.disconnect()





