#!/usr/bin/python3
"""This script lists all cities in a database"""

import MySQLdb
import sys

if __name__ == "__main__":
    av = sys.argv

    query = "SELECT cities.id,cities.name FROM cities JOIN states ON\
            cities.state_id=states.id WHERE states.name LIKE\
            BINARY %s ORDER BY id ASC"
    connection = MySQLdb.connect(user=av[1], passwd=av[2], database=av[3],
                                 port=3306, host="localhost")
    c = connection.cursor()
    c.execute(query, (av[4],))
    rows = c.fetchall()
    for entry in rows:
        print(entry)

