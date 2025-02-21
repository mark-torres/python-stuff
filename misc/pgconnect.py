#!/usr/bin/env python3
# = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = =
#import sys
#sys.path.append("/path/to/custom/modules")
from configparser import ConfigParser
import psycopg2
from pgutils import PgUtils
# = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = =
# = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = =
def config(filename, section):
	# create a parser
	parser = ConfigParser()
	# read config file
	parser.read(filename)

	# get section, default to postgresql
	db = {}
	if parser.has_section(section):
		params = parser.items(section)
		for param in params:
			db[param[0]] = param[1]
	else:
		print('Section {0} not found in the {1} file'.format(section, filename))
	return db

conn = None
try:
	# load connection configuration
	conn_params = config('../ignored/databases.ini', 'produccion')
	# Establish a connection
	conn = psycopg2.connect(**conn_params)

	db = PgUtils(conn)

	# Execute a query
	sql = "SELECT VERSION()"

	# Fetch and print all results
	for row in db.queryRows(sql):
	    print(row)
except Exception as e:
	print("Error connecting to the database: ", e)

if conn is not None:
	# close connection
	conn.close()
