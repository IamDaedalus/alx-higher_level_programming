#!/usr/bin/python3
""" Script to list all states that start with N
htbn_0e_0_usa in ascending order """

import MySQLdb
import sys

if __name__ == "__main__":
    av = sys.argv

    query = "SELECT * FROM states WHERE name LIKE 'N%' ORDER BY id ASC"
    connection = MySQLdb.connect(user=av[1], passwd=av[2], database=av[3],
                                 port=3306, host="localhost")
    c = connection.cursor()
    c.execute(query)
    rows = c.fetchall()
    for entry in rows:
        print(entry)
