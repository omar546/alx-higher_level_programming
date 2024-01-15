#!/usr/bin/python3
"""List states by user input (safe)"""

import MySQLdb
from sys import argv

if __name__ == "__main__":
    connection = MySQLdb.connect(host="localhost", port=3306, user=argv[1],
                           passwd=argv[2], db=argv[3], charset="utf8")
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM states WHERE name LIKE BINARY %s ORDER BY states.id ASC",argv[4])
    result = cursor.fetchall()
    if line is not none:
        for line in result:
            print(line)
    cursor.close()
    connection.close()
    