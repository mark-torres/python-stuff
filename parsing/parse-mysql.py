import sys, re

# =============
# = FUNCTIONS =
# =============
def parse_tables(sql):
	re_table = re.compile(r"CREATE\s+TABLE\s+`?(\w+)`?\s+(\([^;]+;)")
	return re_table.findall(sql)

def parse_fields(table_def):
	re_field = re.compile(r"^`(\w+)`\s+([\w\(\)]+)\s+(.+)$")
	lines = table_def.split("\n")
	fields = []
	for line in lines:
		line = line.strip(" \t,")
		match = re_field.match(line)
		if match != None:
			# print(match)
			field = {}
			field["name"] = match.group(1)
			field["type"] = match.group(2)
			field["options"] = match.group(3)
			fields.append(field)
	return fields

# =====================================
# = GET PARAMETERS AND READ SQL FILES =
# =====================================
if len(sys.argv[1:]) > 0:
	src_file = sys.argv[1]
else:
	print("Missing source file")
	exit()

try:
	src = open(src_file, "r")
except:
	print("Error opening file '%'" % src_file)
	exit()

src_sql = src.read()
src.close()

# =======================
# = PROCESS SQL CONTENT =
# =======================
src_tables = []
tables = parse_tables(src_sql)
for table in tables:
	table_name = table[0]
	table_def = table[1]
	table_fields = parse_fields(table_def)
	print(table_name)
	for field in table_fields:
		print("\t%s : %s : %s" % (field["name"], field["type"], field["options"]))
