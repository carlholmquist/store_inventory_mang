import sqlite3
import json
from config_manage import dbdir
from sqlite3 import Error
from connect_db import create_connection

def create_item(connection,create_item,item):
    try:
        connection.cursor().execute(create_item, item)
        connection.commit()
        print('item created')
    except Error as e:
        print('item not created: ',e)

def main (item_list):
    connection = create_connection(dbdir())

    sql_insert_instruction = """ INSERT INTO items (item_cat,item_brand)
                                 VALUES(?,?); """

    if connection != None:
        create_item(connection,sql_insert_instruction,item_list)
