#!/usr/bin/python3
"""List states by user input"""

import MySQLdb
from sys import argv

if __name__ == "__main__":
    connection = MySQLdb.connect(host="localhost", port=3306, user=argv[1],
                                 passwd=argv[2], db=argv[3], charset="utf8")
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM states \
                   WHERE name LIKE BINARY '{}' \
                   ORDER BY states.id ASC".format(argv[4]))
    result = cursor.fetchall()
    for line in result:
        if line[1].startswith("N"):
            print(line)
    cursor.close()
    connection.close()
