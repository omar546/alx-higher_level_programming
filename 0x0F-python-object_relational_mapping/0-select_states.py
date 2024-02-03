#!/usr/bin/python3
"""List states"""

import MySQLdb
from sys import argv

if __name__ == "__main__":
    connection = MySQLdb.connect(host="localhost", port=3306, user=argv[1],
                                 passwd=argv[2], db=argv[3], charset="utf8")
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM states ORDER BY states.id ASC")
    result = cursor.fetchall()
    for line in result:
        print(line)
    cursor.close()
    connection.close()
