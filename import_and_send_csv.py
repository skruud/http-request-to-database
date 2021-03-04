import requests
import csv
import json
from sql_database import SQLDatabase

tables = ['sector', 'occupation', 
          'form', 'industry', 'role', 
          'duration']

c = open('olddata2.csv', 'r', encoding='utf-8-sig')
data = csv.DictReader(c)

database = SQLDatabase()
for row in data:
    date = row['date'][0:10]
    location = row['location']
    
    category = 'Alle yrker'
    amount = row['totalAds']

    public_table = "public.occupation" 
    columns = "category, amount, date, location"
    values = "'%s', %s, '%s', '%s'" %(category, amount, date, location)
    print(values)
    database.insert_data(public_table, columns, values)

    for table in tables:
        for k, v in json.loads(row[table]).items():
            category = k
            amount = v['N']
            #print(k, v['N'], location, date)
            
            public_table = "public.%s" %(table)
            columns = "category, amount, date, location"
            values = "'%s', %s, '%s', '%s'" %(category, amount, date, location)
            print(values)
            database.insert_data(public_table, columns, values)


database.disconnect()





