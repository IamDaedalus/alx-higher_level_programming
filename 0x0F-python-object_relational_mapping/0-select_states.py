#!/usr/bin/python3
""" Script to list all states from a table states in database
htbn_0e_0_usa in ascending order """

import MySQLdb
import sys

if __name__ == "__main__":
    av = sys.argv

    with MySQLdb.connect(user=av[1], passwd=av[2],
                         database=av[3], host="localhost",  port="3306") as db:
        with db.cursor() as c:
            c.execute("SELECT id,name FROM states ORDER BY id ASC")
            rows = c.fetchall()
            for entry in rows:
                print(entry)
