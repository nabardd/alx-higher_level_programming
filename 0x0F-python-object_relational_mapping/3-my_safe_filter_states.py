#!/usr/bin/python3

"""
Takes in an argument and displays all values in
the states tabel of hbtn_0e_0 where name matches
the argument.

Safe from SQL Injection

The script accepts four arguments:
	-- mysql username,
	-- mysql password,
	-- database name,
    -- state name searched
"""

import sys
import MySQLdb

def db_connect():
    """
    Connects to the database and queries it
    based on file function
    """

    try:
        db = MySQLdb.connect(
            host="localhost", 
            port=3306,
            user=sys.argv[1],
            password=sys.argv[2],
            database=sys.argv[3]
        )
    except Exception as e:
        print(f"Could not connect to the database. {e}")
        return 0

    cursor = db.cursor()

    query = """
    SELECT * FROM `states`
    WHERE name = %s
    ORDER BY id ASC
    """
    cursor.execute(query, sys.argv[4])
    results = cursor.fetchall()

    for state in results:
        print(state)
    
    cursor.close()
    db.close()


if __name__ == "__main__":
    db_connect()
