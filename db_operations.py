#!/usr/bin/python
import psycopg2
from settings.config import config


def bulk_insert_sales(items):
    """ Connect to the PostgreSQL database server """
    connection = None
    try:
        # read connection parameters
        params = config()

        # connect to the PostgreSQL server
        print('Connecting to the PostgreSQL database...')
        connection = psycopg2.connect(**params)

        # create a cursor
        cursor = connection.cursor()

        # create request
        sql_insert_query = """ INSERT INTO sale (product, quantity, price)
                           VALUES (%s,%s,%s) """

	    # execute a statement
        # executemany() to insert multiple rows rows
        result = cursor.executemany(sql_insert_query, items)
        connection.commit()
        print(cursor.rowcount, "Record inserted successfully into sale table")

	    # close the communication with the PostgreSQL
        cursor.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print("Failed inserting record into sale table {}".format(error))
    finally:
        if connection is not None:
            connection.close()
            print('Database connection closed.')
