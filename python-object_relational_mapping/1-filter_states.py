#!/usr/bin/python3
"""
Lists all states with a name starting with N
"""

import sys
import MySQLdb

if __name__ == "__main__":
    mySQL_u = sys.argv[1]
    mySQL_p = sys.argv[2]
    db_name = sys.argv[3]

    # By default, it will connect to localhost:3306 i think
    db = MySQLdb.connect(user=mySQL_u, passwd=mySQL_p, db=db_name)
    c = db.cursor()

    c.execute("SELECT * FROM states WHERE name LIKE BINARY 'N%' ORDER BY id")
    rows = c.fetchall()

    for row in rows:
        print(row)
