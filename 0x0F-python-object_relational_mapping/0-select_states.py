#!/usr/bin/python3
"""
Lists all states from the database hbtn_0e_usa,
the script accepts three arguments:
	-- mysql username,
	-- mysql password,
	-- database name
"""

import sys
import MySQLdb


def db_connect():
	try:
		db = MySQLdb.connect(
			host="localhost", 
			port=3306,
        	user=sys.argv[1],
        	password=sys.argv[2],
        	database=sys.argv[3],
		)
	except Exception as e:
		print(f"Could not connect to the database: {e}")
		return 0

	print("Connected")

	cursor = db.cursor()
	query = """
	SELECT * FROM `states`
	ORDER BY id ASC
	"""
	cursor.execute(query)

	results = cursor.fetchall()

	for state in results:
		print(state)

	cursor.close()
	db.close()


if __name__ == "__main__":
	db_connect()
