#!/usr/bin/python3
"""Script that lists all states from the database hbtn_0e_0_usa"""

import MySQLdb
from sys import argv

if __name__ == "__main__":
        """Conection to the DataBase"""
        db = MySQLdb.connect(host="localhost", port=3306, 
                             user=argv[1], 
                             password=argv[2], 
                             db=argv[3])
        
        """Cursor excecutes the SQL queries"""
        cursor = db.cursor()
        command = "SELECT * FROM states WHERE name LIKE '{}' ORDER BY id ASC;".format(argv[4])
        cursor.execute(command)
        rows = cursor.fetchall()
        
        for x in rows:
                print(x)
        
        cursor.close()
        db.close()