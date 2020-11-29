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
    """
    -----------------------------------
    prints total quantitys for products
    -----------------------------------
    """
    stock_tuples = []
    connection = sqlite3.connect('store.db')
    cursor = connection.cursor()

    for row in cursor.execute('SELECT * FROM warehouse ORDER BY product'):
        stock_tuples.append(row)

    connection.close()

    stock_dict = {}

    for row in stock_tuples:
        if row[0] not in stock_dict.keys():
            stock_dict[row[0]] = row[1]
        else:
            stock_dict[row[0]] += row[1]

    print()
    for key in stock_dict:
        print("{:10s} {:8d}" .format(key, stock_dict[key]),
              '\n{}'.format('-' * 19))


def purchase_order():
    """
    ------------------------
    receiving goods function
    ------------------------
    """

    vendor = ''
    rec_shipment_doc = ''

    while vendor == '' or rec_shipment_doc == '':

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

        error = False

        print('{}. product name'.format(iterator), end='')
        product = str.upper(input(' >>> '))
        if product == '':
            error = True

        clear()

        print('{}. {} quantity'.format(iterator, product), end='')
        try:
            quantity = int(input(' >>> '))
        except ValueError:
            error = True
            quantity = 0

        clear()

        if error is False:
            receiving_showup += ('\n{}. {} {}'
                                 .format(iterator, product, quantity))

        print(receiving_showup)

        if error is True:
            print('X. {} {}   Ooops! Something is missing. Try again'
                  .format(product, quantity))
            iterator -= 1

        print('\n\nPress ENTER to continue'
              "\nType 'END' to submit.\nType 'DEL' to abort.")

        # print all received goods

        if error is False:
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

        clear()
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
        elif ingerence == 'exit' or ingerence == 'quit':
            clear()
            sys.exit(0)
        else:
            break


def data_interface():

    ingerence = ''
    while True:

        if ingerence != '1':
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
            elif ingerence == 'exit' or ingerence == 'quit':
                clear()
                sys.exit(0)
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
            clear()
            sys.exit(0)


if __name__ == '__main__':

    print(f"""\nSQLite3 module ver.{sqlite3.version}
SQLite library ver.{sqlite3.sqlite_version}""")

    connection = sqlite3.connect('store.db')
    cursor = connection.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS warehouse\
                   (product TEXT, quantity INTEGER, date TEXT,\
                    location TEXT, vendor TEXT, shipment_doc TEXT)")
    connection.close()

    while True:
        main_menu()
