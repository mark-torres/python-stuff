import sqlite3

class MyDB:
	def __init__(self, db_file):
		self.conn = sqlite3.connect(db_file)
		self.conn.row_factory = sqlite3.Row
		self.cursor = self.conn.cursor()

	def __del__(self):
		self.conn.close()

	def query(self, query):
		self.cursor.execute(query)

	def fetchall(self):
		return self.cursor.fetchall()

	def fetchone(self):
		return self.cursor.fetchone()

