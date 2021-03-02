from sql_database import SQLDatabase
import matplotlib.pyplot as plt

database = SQLDatabase()


sql = """SELECT amount, date
         FROM PUBLIC.occupation
         WHERE category LIKE 'Butikka%' AND location = 'Oslo'
         ORDER BY date;"""
db_response = database.retrieve_sql_data(sql)
database.disconnect()

#print(db_response[0:39][0])
x_ = []
y_ = []
for y, x in db_response:
    x_.append(x)
    y_.append(y)
    print(x)
plt.plot(x_, y_)
    
plt.show()







