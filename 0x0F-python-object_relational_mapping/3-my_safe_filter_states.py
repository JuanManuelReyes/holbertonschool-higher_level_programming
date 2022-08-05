#!/usr/bin/python3
"""
Script that takes in arguments and displays all values in the 
states table of hbtn_0e_0_usa where name matches the argument. 
But this time, write one that is safe from MySQL injections!
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
        command = "SELECT * FROM states WHERE name=%s ORDER BY id ASC;"
        cursor.execute(command, (argv[4],))
        rows = cursor.fetchall()
        
        for x in rows:
                print(x)
        
        cursor.close()
        db.close()
        