from sql_database import SQLDatabase

database = SQLDatabase()

#retrieve_data(select, table, where, order):
select = 'category, amount, date'
table = 'occupation'
where = "location = 'Oslo', category = 'Arkivar'"
order = 'date'

database.retrieve_data(select, table, where, order)
database.disconnect()