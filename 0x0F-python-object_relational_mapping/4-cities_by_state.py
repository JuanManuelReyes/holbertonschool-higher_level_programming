#!/usr/bin/python3
"""
Script that lists all cities from the database hbtn_0e_4_usa
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
        cursor.execute("SELECT cities.id, cities.name, states.name \
                       FROM states \
                       INNER JOIN cities ON states.id = cities.state_id \
                       ORDER BY cities.id ASC;")
        rows = cursor.fetchall()
        
        for x in rows:
                print(x)
        
        cursor.close()
        db.close()