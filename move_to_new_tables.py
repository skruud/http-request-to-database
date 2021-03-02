from sql_database import SQLDatabase

database = SQLDatabase()

table = 'duration'

sql = """SELECT
            name, id
        FROM
            %s_names;""" %(table)
db_names = database.retrieve_sql_data(sql)

sql = """SELECT
            category, amount, date, location
        FROM
            %s
        ORDER BY
            date;""" %(table)
db_response = database.retrieve_sql_data(sql)

for name in db_names:
    print(name)

names_dict = dict(db_names)
print(names_dict['Lærling'])

#print(db_response[0:39][0])

for row in db_response:
    print("%s, %s, %s, %s" %(names_dict[row[0]], row[1], row[2], row[3]))
    





for row in db_response:
    public_table = "public.%s_test" %(table)
    columns = "category, amount, date, location"
    values = "'%s', '%s', '%s', '%s'" %(names_dict[row[0]], row[1], row[2], row[3])

    database.insert_data(public_table, columns, values)


database.disconnect()



