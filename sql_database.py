import psycopg2
from config import config

class SQLDatabase:

    def __init__(self):
        connect()

    def connect(self):
        self.conn = None
        #vendor_id = None
        try:
            # read database configuration
            params = config()
            # connect to the PostgreSQL database
            self.conn = psycopg2.connect(**params)
            # create a new cursor
            self.cur = conn.cursor()
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
            self.cur.close()
            if self.conn is not None:
                self.conn.close()

    def disconnect(self):
        try:
            # commit the changes to the database
            self.conn.commit()
            # close communication with the database
            self.cur.close()
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
        finally:
            if conn is not None:
                self.conn.close()

    def insert_data(self, table, columns, values):
        """ insert a new vendor into the vendors table """
        sql = """INSERT INTO {table}({columns})
                VALUES({values}) RETURNING vendor_id;""".format(table, columns, values)
        
        try:
            # execute the INSERT statement
            self.cur.execute(sql, (vendor_name,))
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
            self.cur.close()
            if conn is not None:
                self.conn.close()
        
