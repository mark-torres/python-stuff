
class PgUtils:
	"""docstring for PgUtils"""
	def __init__(self, pg_conn):
		self.conn = pg_conn
		self.logs = []
		self.errors = []

	def queryCursor(self, sql):
		cur = self.conn.cursor()
		cur.execute(sql)
		self.saveLog(sql)
		return cur

	def queryRows(self, sql):
		cur = self.queryCursor(sql)
		rows = []
		if cur.rowcount > 0:
			for row in cur:
				rows.append(row)
		cur.close()
		return rows

	def queryRow(self, sql):
		cur = self.queryCursor(sql)
		row = None
		if cur.rowcount > 0:
			row = cur.fetchone()
		return row

	def saveLog(self, log):
		self.logs.append(log)

	def saveError(self, error):
		self.errors.append(error)
