#import psycopg2
#from config import config
import requests
import json



sql = """INSERT INTO vendors(vendor_name)
         VALUES(%s) RETURNING vendor_id;"""
#insert_vendor(sql)

data_link = 'https://8syg62n83a.execute-api.eu-north-1.amazonaws.com/dev/vd'

x = requests.get(data_link)
data = x.json()
print(data[0]['date'])





