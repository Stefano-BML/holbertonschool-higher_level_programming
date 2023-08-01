#!/usr/bin/python3
"""
Script that lists all values in the `states` table of `hbtn_0e_0_usa`
where `name` matches the argument `state name searched`.
"""

import sys
import MySQLdb

if __name__ == "__main__":
    mySQL_u = sys.argv[1]
    mySQL_p = sys.argv[2]
    db_name = sys.argv[3]

    searched_name = sys.argv[4]

    # By default, it will connect to localhost:3306
    db = MySQLdb.connect(user=mySQL_u, passwd=mySQL_p, db=db_name)
    c = db.cursor()

    c.execute("SELECT * FROM states WHERE name LIKE BINARY '{}' ORDER BY id"
                .format(searched_name))
    rows = c.fetchall()

    for row in rows:
        print(row)
