from sql_database import SQLDatabase

database = SQLDatabase()


sql = """SELECT
            DISTINCT category 
        FROM
            sector
        ORDER BY
            category;"""
db_response = database.retrieve_sql_data(sql)


#print(db_response[0:39][0])
x_ = []
for x in db_response:
    x_.append(x[0])

x_.sort()
print(x_)

name_list = x_

for row in name_list:
    public_table = "public.sector_names" 
    columns = "name"
    values = "'%s'" %(row)

    database.insert_data(public_table, columns, values)


database.disconnect()



