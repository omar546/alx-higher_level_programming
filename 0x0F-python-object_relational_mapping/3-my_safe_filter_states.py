#!/usr/bin/python3
"""retrive all states"""
import MySQLdb
import sys


if __name__ == '__main__':
    args = sys.argv
    if len(args) < 5:
        print("Usage: {} username password db_name state_name".format(args[0]))
        exit(1)
    name = args[1]
    passwd = args[2]
    dbName = args[3]
    state_name = args[4]
    dataBase = MySQLdb.connect(host='localhost', user=name,
                         passwd=passwd, db=dbName,
                         port=3306)
    cursor = dataBase.cursor()
    nrows = cursor.execute("SELECT * FROM states ORDER BY states.id")
    all = cursor.fetchall()
    for one in all:
        if (state_name == one[1]):
            print(one)
