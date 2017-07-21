# -*- coding: utf-8 -*-
from mysql.connector import MySQLConnection, Error


def call_find_all_sp():
    try:
        conn = MySQLConnection(user='root',
                               password='1',
                               host='127.0.0.1',
                               database='Users')
        cursor = conn.cursor()

        cursor.callproc('create_tables')

        # print out the result
        for result in cursor.stored_results():
            print(result.fetchall())

    except Error as e:
        print(e)

    finally:
        cursor.close()
        conn.close()


if __name__ == '__main__':
    call_find_all_sp()
