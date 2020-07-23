import sqlite3
from config_manage import dbdir
from sqlite3 import Error
from connect_db import create_connection

def create_table(connection,create_table_sql):
    try:
        connection.cursor().execute(create_table_sql)
        print('Table created')
    except Error as e:
        print('Table not created: ',e)

def main ():
    connection = create_connection(dbdir())

    sql_create_items_table = """ CREATE TABLE IF NOT EXISTS items (
                                        item_id integer PRIMARY KEY,
                                        item_cat text NOT NULL,
                                        item_brand text
                                    ); """

    if connection != None:
        create_table(connection,sql_create_items_table)

main()