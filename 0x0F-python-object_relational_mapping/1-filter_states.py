#!/usr/bin/python3
"""
Script that lists all states with a name starting 
with N (upper N) from the database hbtn_0e_0_usa
"""

import MySQLdb
from sys import argv

if __name__ == "__main__":
    """Conection to the DataBase"""
    db = MySQLdb.connect(host="localhost", port=3306,
                         user=argv[1],
                         passwd=argv[2],
                         db=argv[3])

    """Cursor excecutes the SQL queries"""
    cursor = db.cursor()
    cursor.execute(
        "SELECT * FROM states WHERE name LIKE 'N%' ORDER BY id ASC;")
    rows = cursor.fetchall()

    for x in rows:
        print(x)

    cursor.close()
    db.close()
