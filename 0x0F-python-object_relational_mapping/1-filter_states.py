#!/usr/bin/python3

"""
Lists all states with a name starting with N from
the database hbtn_0e_0_usa.

The script accepts three arguments:
	-- mysql username,
	-- mysql password,
	-- database name
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
    WHERE name LIKE 'N%'
    ORDER BY id ASC
    """
    cursor.execute(query)
    results = cursor.fetchall()

    for state in results:
        print(state)


if __name__ == "__main__":
    db_connect()
