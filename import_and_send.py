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

tables = ['sector', 'occupation', 
          'form', 'industry', 'role', 'duration']

#Correct displaced items
sector_categories = ['Franchise/Selvstendig næringsdrivende', 
                     'Offentlig', 'Privat', 'Samvirke', 'Organisasjoner']
form_categories = ['Heltid', 'Deltid']
role_categories = ['Leder', 'Direktør', 'Fagleder']
due_categories = ['Siste frist', 'Under en uke', 'Under tre døgn']

database = SQLDatabase()

for date_and_location in data:
    for table in tables:
        for element in date_and_location[table]:
            amount = date_and_location[table][element]
            date = date_and_location['date'][0:10]
            location = date_and_location['location']

            public_table = "public.%s" %(table)
            if element in sector_categories and table == 'role':
                public_table = "public.sector" 
            if element in form_categories and table == 'duration':
                public_table = "public.form" 
            if element in role_categories and table == 'sector':
                public_table = "public.role" 

            if element not in due_categories:
                columns = "category, amount, date, location"
                values = "'%s', %s, '%s', '%s'" %(element, amount, date, location)

                database.insert_data(public_table, columns, values)

database.disconnect()





