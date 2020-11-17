# -*- coding: utf-8 -*-
import sqlite3
import sys
from os import system, name


def clear():

    system('clear' if name == 'posix' else 'cls')


def purchase_order():

    print('\nInput receiving shipment document number.', end='')
    rec_shipment_doc = str.upper(input(' >>> '))

    print('\nInput vendor name.', end='')
    vendor = str.title(str.lower(input(' >>> ')))

    clear()

    data_tuple_list = []
    iterator = 1

    print('{}. part number'.format(iterator), end='')
    product = str.upper(input(' >>> '))
    clear()

    print('{}. {} lot'.format(iterator, product), end='')
    lot = str.upper(input(' >>> '))
    clear()

    print('{}. {} {} quantity'.format(iterator, product, lot), end='')
    quantity = int(input(' >>> '))
    clear()

    print('{}. {} {} {}' .format(iterator, product, lot, quantity))

    location = 'RECEIVING_HUB'
    # wares have to be trasfered manually after receiving

    data_tuple_list.append((product, quantity, lot, location, vendor,
                            rec_shipment_doc))

    for data_tuple in data_tuple_list:
        cursor.execute("INSERT INTO warehouse VALUES (?,?,?,?,?,?)",
                       data_tuple)
        connection.commit()


def operations_interface():

    while True:

        clear()

        print("""
    1 - internal transfer
    2 - purchase order
    3 - make shipment
other - go back""")

        ingerence = input('>>> ')

        if ingerence == '1':
            break
        elif ingerence == '2':
            purchase_order()
            break
        elif ingerence == '3':
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
            ingerence = input('>>> ')

            if ingerence == '1':
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
exit -  exit program""")

        ingerence = input('>>> ')

        if ingerence == '1':
            operations_interface()
            break
        elif ingerence == '2':
            data_interface()
            break
        elif ingerence == 'exit' or ingerence == 'quit':
            sys.exit(0)


if __name__ == '__main__':

    connection = sqlite3.connect('store.db')

    cursor = connection.cursor()

    cursor.execute("CREATE TABLE IF NOT EXISTS warehouse \
        (part_number TEXT PRIMARY KEY, quantity REAL, lot TEXT, \
        location TEXT, vendor TEXT, shipment_doc TEXT)")

    while True:
        main_menu()

    connection.close()
