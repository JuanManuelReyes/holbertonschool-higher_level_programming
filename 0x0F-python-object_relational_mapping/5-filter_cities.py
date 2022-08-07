#!/usr/bin/python3
"""
Script that takes in the name of a state as an argument and lists
all cities of that state, using the database hbtn_0e_4_usa
"""

from sqlite3 import SQLITE_CREATE_INDEX
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
    command = "SELECT name FROM cities \
                WHERE state_id = (SELECT id FROM states WHERE name = %s) \
                        ORDER BY id ASC;"
    cursor.execute(command, (argv[4],))
    rows = cursor.fetchall()

    for x in range(len(rows)):
        if (x != len(rows) - 1):
            print(rows[x][0], end=", ")
        else:
            print(rows[x][0], end="")

    print("")
    cursor.close()
    db.close()
