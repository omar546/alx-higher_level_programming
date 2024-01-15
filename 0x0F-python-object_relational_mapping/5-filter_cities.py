#!/usr/bin/python3
"""List cities by user input state in database"""

import MySQLdb
from sys import argv

if __name__ == "__main__":
    connection = MySQLdb.connect(host="localhost", port=3306, user=argv[1],
                           passwd=argv[2], db=argv[3], charset="utf8")
    cursor = connection.cursor()
    cursor.execute("""
            SELECT
                cities.id, cities.name, states.name
            FROM
                cities
            JOIN
                states
            ON
                cities.state_id = states.id
            WHERE states.name LIKE BINARY %s
            ORDER BY
                cities.id ASC
        """,argv[4])
    result = cursor.fetchall()
    if result is not None:
        print(", ".join([line[1] for line in result]))

    cursor.close()
    connection.close()
    