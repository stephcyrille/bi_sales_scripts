#!/usr/bin/python
import psycopg2
from settings.config import config


def insert_invoice(item):
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
        sql_insert_query = """ INSERT INTO invoices (ref, name, total_price)
                           VALUES (%s,%s,%s) """

	    # execute a statement
        # executemany() to insert multiple rows rows
        cursor.execute(sql_insert_query, item)
        id_invoice = cursor.fetchone()[0]
        connection.commit()
        print("THE ID OF THE SAVED INVOICE IS", id_invoice)

	    # close the communication with the PostgreSQL
        cursor.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print("Failed inserting record into invoice table {}".format(error))
    finally:
        if connection is not None:
            connection.close()
            print('Database connection closed.')

def bulk_insert_invoices(items):
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
        sql_insert_query = """ INSERT INTO invoices (ref, name, total_price)
                           VALUES (%s,%s,%s) """

	    # execute a statement
        # executemany() to insert multiple rows rows
        result = cursor.executemany(sql_insert_query, items)
        connection.commit()
        print(cursor.rowcount, "Record inserted successfully into invoices table")

	    # close the communication with the PostgreSQL
        cursor.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print("Failed inserting record into invoices table {}".format(error))
    finally:
        if connection is not None:
            connection.close()
            print('Database connection closed.')


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
        sql_insert_query = """ INSERT INTO sale (product, quantity, price, city)
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

