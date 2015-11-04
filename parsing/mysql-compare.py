#!/usr/bin/python
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
	fields = {}
	for line in lines:
		line = line.strip(" \t,")
		match = re_field.match(line)
		if match != None:
			fields[match.group(1)] = {"type":match.group(2), "options":match.group(3)}
	return fields

def compare_table(src_table, dst_table):
	table_diff = {}
	src_fields = src_table["fields"].keys()
	dst_fields = dst_table["fields"].keys()
	src_set = set(src_fields)
	dst_set = set(dst_fields)
	table_diff["to_del"] = dst_set.difference(src_set)
	table_diff["to_add"] = src_set.difference(dst_set)
	common = src_set.intersection(dst_set)
	changed = {}
	for field in common:
		src_field = src_table["fields"][field]
		dst_field = dst_table["fields"][field]
		
		if src_field["type"] == dst_field["type"]:
			ch_type = False
		else:
			ch_type = True
		
		if src_field["options"] == dst_field["options"]:
			ch_opts = False
		else:
			ch_opts = True
		
		if ch_type or ch_opts:
			changed[field] = {}
			if ch_opts:
				changed[field]["options"] = {"src":src_field["options"], "dst":dst_field["options"]}
			if ch_type:
				changed[field]["type"] = {"src":src_field["type"], "dst":dst_field["type"]}
	table_diff["changed"] = changed
	return table_diff

def print_field(field_name, field_data):
	fstring = "%-20s | %-13s | %-40s"
	print(fstring % (field_name, field_data["type"], field_data["options"]))

def print_change(table_change):
	fields = table_change.keys()
	fstring = "%-20s | %-13s | %-40s | %-40s"
	print( '-'*21 + '+' + '-'*15 + '+' + '-'*42 + '+' + '-'*41 )
	print(fstring % ('FIELD NAME', 'CHANGE TYPE', 'CURRENT', 'UPDATED'))
	for field in fields:
		field_changes = table_change[field].keys()
		field_name = field
		for field_change in field_changes:
			if field_name != '':
				print( '-'*21 + '+' + '-'*15 + '+' + '-'*42 + '+' + '-'*41 )
			print(fstring % \
				(field_name, field_change, table_change[field][field_change]["dst"], table_change[field][field_change]["src"]))
			field_name = ''
	print( '-'*21 + '+' + '-'*15 + '+' + '-'*42 + '+' + '-'*41 )
	print("")

# =====================================
# = GET PARAMETERS AND READ SQL FILES =
# =====================================
if len(sys.argv[1:]) > 0:
	src_file = sys.argv[1]
else:
	print("Missing source file")
	exit()

if len(sys.argv[2:]) > 0:
	dst_file = sys.argv[2]
else:
	print("Missing destination file")
	exit()

try:
	src = open(src_file, "r")
except:
	print("Error opening file '%'" % src_file)
	exit()

try:
	dst = open(dst_file, "r")
except:
	src.close()
	print("Error opening file '%'" % dst_file)
	exit()

src_sql = src.read()
dst_sql = dst.read()

src.close()
dst.close()

# =======================
# = PROCESS SQL CONTENT =
# =======================

src_tables = {}
src_table_names = []
dst_tables = {}
dst_table_names = []

# parse source file
tables = parse_tables(src_sql)
for table in tables:
	table_name = table[0]
	src_table_names.append(table_name)
	table_def = table[1]
	table_fields = parse_fields(table_def)
	src_tables[table_name] = {"fields":table_fields}

# parse source file
tables = parse_tables(dst_sql)
for table in tables:
	table_name = table[0]
	dst_table_names.append(table_name)
	table_def = table[1]
	table_fields = parse_fields(table_def)
	dst_tables[table_name] = {"fields":table_fields}

# =======================
# = PROCESS DIFFERENCES =
# =======================
src_set = set(src_table_names)
dst_set = set(dst_table_names)

common_tables = src_set.intersection(dst_set)
tables_to_delete = dst_set.difference(src_set)
tables_to_create = src_set.difference(dst_set)
table_diffs = {}

print("")
print("CHANGED (COMMON TABLES):")
for table in common_tables:
	table_diffs[table] = compare_table(src_tables[table], dst_tables[table])
	changed = table_diffs[table]["changed"]
	to_del = table_diffs[table]["to_del"]
	to_add = table_diffs[table]["to_add"]
	if len(changed) or len(to_add) or len(to_del):
		print("%s %s" % ('#'*30, table))
		fstring = "%-20s | %-13s | %-40s"
		if len(changed) > 0:
			print("FIELDS TO MODIFY")
			print_change(changed)
		if len(to_add) > 0:
			print("FIELDS TO ADD")
			print( '-'*21 + '+' + '-'*15 + '+' + '-'*42 )
			print(fstring % ('FIELD NAME', 'TYPE', 'OPTIONS'))
			print( '-'*21 + '+' + '-'*15 + '+' + '-'*42 )
			for field in to_add:
				print_field(field, src_tables[table]["fields"][field])
			print( '-'*21 + '+' + '-'*15 + '+' + '-'*42 )
		if len(to_del) > 0:
			print("FIELDS TO DELETE")
			print( '-'*21 + '+' + '-'*15 + '+' + '-'*42 )
			print(fstring % ('FIELD NAME', 'TYPE', 'OPTIONS'))
			print( '-'*21 + '+' + '-'*15 + '+' + '-'*42 )
			for field in to_del:
				print_field(field, dst_tables[table]["fields"][field])
			print( '-'*21 + '+' + '-'*15 + '+' + '-'*42 )
		print("")
print("")
if len(tables_to_delete) > 0:
	print("- - - - - - - - - - - - - - - - - - - - - - - ")
	print("TO DELETE (IN DESTINATION BUT NOT IN SOURCE):")
	print(tables_to_delete)
if len(tables_to_create) > 0:
	print("- - - - - - - - - - - - - - - - - - - - - - - ")
	print("TO CREATE (IN SOURCE BUT NOT IN DESTINATION):")
	print(tables_to_create)