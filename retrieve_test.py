from sql_database import SQLDatabase

database = SQLDatabase()

#retrieve_data(self, select, table, where, order):
select = 'category, amount, date'
table = 'sector'
where = 'Innlandet'
order = 'date'

database.retrieve_data(select, table, where, order)
database.disconnect()