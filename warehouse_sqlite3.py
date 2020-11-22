# -*- coding: utf-8 -*-
import sqlite3
import sys
from os import system, name
from datetime import date

"""
Main function:
   * creates storage file if does not exist
   * runs infinite loop with basic terminal interface as functions tree
   * at the end of functions tree are called database operation modules
"""


def clear():

    system('clear' if name == 'posix' else 'cls')


def make_shipment():
    pass


def internal_transfer():
    pass


def stock_status():

    class Product:
        def __init__():
            # self.product
            # self.quantity
            # self.data_date
            # self.location
            # self.vendor
            # self.rec_shipment_doc
            pass

    stock = []

    connection = sqlite3.connect('store.db')
    cursor = connection.cursor()

    for row in cursor.execute('SELECT * FROM warehouse ORDER BY product'):
        stock.append(row)

    connection.close()


def purchase_order():
    """
    receiving goods function
    """

    print('\nInput vendor name.', end='')
    vendor = str.title(str.lower(input(' >>> ')))

    print('\nInput receiving shipment document number.', end='')
    rec_shipment_doc = str.upper(input(' >>> '))

    clear()

    location = 'RECEIVING_HUB'  # default value
    data_tuple_list = []
    iterator = 1
    receiving_showup = ''
    data_date = date.strftime(date.today(), '%Y.%m.%d')

    while iterator:

        print('{}. product name'.format(iterator), end='')
        product = str.upper(input(' >>> '))
        clear()

        print('{}. {} quantity'.format(iterator, product), end='')
        quantity = int(input(' >>> '))
        clear()

        receiving_showup += ('{}. {} {}\n'
                             .format(iterator, product, quantity))

        print(receiving_showup + '\n\nPress ENTER to continue'
              "\nType 'END' to submit.\nType 'DEL' to abort.")
        # print all received goods

        data_tuple_list.append((product, quantity, data_date, location,
                                vendor, rec_shipment_doc))
        ingerence = str.strip(str.upper(input(' >>> ')))

        if ingerence == '':
            pass

        elif ingerence == 'END':

            connection = sqlite3.connect('store.db')
            cursor = connection.cursor()
            cursor.executemany("INSERT INTO warehouse VALUES (?,?,?,?,?,?)",
                               data_tuple_list)
            connection.commit()
            connection.close()
            break

        elif ingerence == 'DEL':
            break

        iterator += 1


def operations_interface():

    while True:

        clear()

        print("""
    1 - internal transfer
    2 - purchase order
    3 - make shipment
other - go back""")

        ingerence = str.strip(input('>>> '))

        if ingerence == '1':
            internal_transfer()
            break
        elif ingerence == '2':
            purchase_order()
            break
        elif ingerence == '3':
            make_shipment()
            break
        else:
            break


def data_interface():

    while True:

        clear()

        print("""
    1 - stock status
    2 - nothing yet
other - go back""")

        while True:
            ingerence = str.strip(input('>>> '))

            if ingerence == '1':
                stock_status()
                break
            elif ingerence == '2':
                break
            else:
                break

        if ingerence != '1' and ingerence != '2':
            break


def main_menu():

    while True:

        clear()

        print("""
   1 - operations
   2 - data
exit -  quit program""")

        ingerence = str.lower(str.strip(input('>>> ')))

        if ingerence == '1':
            operations_interface()
            break
        elif ingerence == '2':
            data_interface()
            break
        elif ingerence == 'exit' or ingerence == 'quit':
            sys.exit(0)


if __name__ == '__main__':

    print(f"""\nSQLite3 module ver.{sqlite3.version}
SQLite library ver.{sqlite3.sqlite_version}""")

    connection = sqlite3.connect('store.db')
    cursor = connection.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS warehouse\
                   (product TEXT, quantity INTERGER, date TEXT,\
                    location TEXT, vendor TEXT, shipment_doc TEXT)")
    connection.close()

    while True:
        main_menu()
