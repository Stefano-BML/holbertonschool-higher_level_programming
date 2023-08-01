#!/usr/bin/python3
""" Data base with states in USA """

import sys
import MySQLdb

if __name__ == '__main__':
    db = MySQLdb.connect(
        host="localhost",
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3],
        port=3306
    )

    c = db.cursor()
    c.execute("SELECT * FROM states;")
    states = c.fetchall()

    for state in states:
        print(state)

    # Close cursor
    c.close()

    # close database
    db.close()
