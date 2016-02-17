#!/usr/bin/env python
import sys, re

# MySQL create table reference:
# https://dev.mysql.com/doc/refman/5.5/en/create-table.html

line_field = '-'*21 + '+' + '-'*15 + '+' + '-'*42
line_field_change = '-'*21 + '+' + '-'*15 + '+' + '-'*42 + '+' + '-'*41
line_index = '-'*21 + '+' + '+' + '-'*42
line_index_change = '-'*21 + '+' + '-'*42 + '+' + '-'*41

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

def parse_indexes(table_def):
	re_index = re.compile(r"^KEY[ ]+`(\w+)`[ ]\(([^)]+)\)$")
	lines = table_def.split("\n")
	indexes = {}
	for line in lines:
		line = line.strip(" \t,")
		match = re_index.match(line)
		if match != None:
			index_cols = match.group(2).replace('`','').split(',')
			indexes[match.group(1)] = {"cols":index_cols}
	return indexes

def compare_tables(src_table, dst_table):
	table_diff = {}
	# compare fields
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
	# compare indexes
	src_indexes = src_table["indexes"].keys()
	dst_indexes = dst_table["indexes"].keys()
	src_set = set(src_indexes)
	dst_set = set(dst_indexes)
	table_diff["ix_to_del"] = dst_set.difference(src_set)
	table_diff["ix_to_add"] = src_set.difference(dst_set)
	common = src_set.intersection(dst_set)
	changed = {}
	for index in common:
		src_index = src_table["indexes"][index]
		dst_index = dst_table["indexes"][index]
		if src_index["cols"] != dst_index["cols"]:
			changed[index] = {"src": src_index["cols"], "dst": dst_index["cols"]}
	table_diff["ix_changed"] = changed
	return table_diff

def print_field(field_name, field_data):
	fstring = "%-20s | %-13s | %-40s"
	print(fstring % (field_name, field_data["type"], field_data["options"]))

def print_index(index_name, index_data):
	fstring = "%-20s | %-40s"
	print(fstring % (index_name, index_data['cols']))

def print_field_change(table_change):
	fields = table_change.keys()
	fstring = "%-20s | %-13s | %-40s | %-40s"
	print( line_field_change )
	print(fstring % ('FIELD NAME', 'CHANGE TYPE', 'CURRENT', 'UPDATED'))
	for field in fields:
		field_changes = table_change[field].keys()
		field_name = field
		for field_change in field_changes:
			if field_name != '':
				print( line_field_change )
			print(fstring % \
				(field_name, field_change, table_change[field][field_change]["dst"], table_change[field][field_change]["src"]))
			field_name = ''
	print( line_field_change )
	print("")

def print_index_change(index_change):
	indexes = index_change.keys()
	fstring = "%-20s | %-40s | %-40s"
	print( line_index_change )
	print(fstring % ('INDEX NAME', 'CURRENT COLS', 'UPDATED COLS'))
	print( line_index_change )
	for index in indexes:
		print(fstring % (index, index_change[index]["dst"], index_change[index]["src"]))
		print( line_index_change )
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
	src_tables[table_name] = {}
	table_fields = parse_fields(table_def)
	src_tables[table_name]["fields"] = table_fields
	table_indexes = parse_indexes(table_def)
	src_tables[table_name]["indexes"] = table_indexes

# parse source file
tables = parse_tables(dst_sql)
for table in tables:
	table_name = table[0]
	dst_table_names.append(table_name)
	table_def = table[1]
	dst_tables[table_name] = {}
	table_fields = parse_fields(table_def)
	dst_tables[table_name]["fields"] = table_fields
	table_indexes = parse_indexes(table_def)
	dst_tables[table_name]["indexes"] = table_indexes

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
	print("%s %s" % ('#'*30, table))
	table_diffs[table] = compare_tables(src_tables[table], dst_tables[table])
	changed = table_diffs[table]["changed"]
	to_del = table_diffs[table]["to_del"]
	to_add = table_diffs[table]["to_add"]
	if len(changed) or len(to_add) or len(to_del):
		fstring = "%-20s | %-13s | %-40s"
		if len(changed) > 0:
			print("FIELDS TO MODIFY")
			print_field_change(changed)
		if len(to_add) > 0:
			print("FIELDS TO ADD")
			print( line_field )
			print(fstring % ('FIELD NAME', 'TYPE', 'OPTIONS'))
			print( line_field )
			for field in to_add:
				print_field(field, src_tables[table]["fields"][field])
			print( line_field )
		if len(to_del) > 0:
			print("FIELDS TO DELETE")
			print( line_field )
			print(fstring % ('FIELD NAME', 'TYPE', 'OPTIONS'))
			print( line_field )
			for field in to_del:
				print_field(field, dst_tables[table]["fields"][field])
			print( line_field )
		print("")
	ix_changed = table_diffs[table]["ix_changed"]
	ix_to_del = table_diffs[table]["ix_to_del"]
	ix_to_add = table_diffs[table]["ix_to_add"]
	if len(ix_changed) or len(ix_to_add) or len(ix_to_del):
		fstring = "%-20s | %-13s | %-40s"
		if len(ix_changed) > 0:
			print("INDEXES TO MODIFY")
			print_index_change(ix_changed)
		if len(ix_to_add) > 0:
			print("INDEXES TO ADD")
			print(line_index)
			for index in ix_to_add:
				print_index(index, src_tables[table]["indexes"][index])
				print(line_index)
		if len(ix_to_del) > 0:
			print("INDEXES TO DELETE")
			print(line_index)
			for index in ix_to_del:
				print_index(index, dst_tables[table]["indexes"][index])
				print(line_index)
print("")
if len(tables_to_delete) > 0:
	print("- - - - - - - - - - - - - - - - - - - - - - - ")
	print("TO DELETE (IN DESTINATION BUT NOT IN SOURCE):")
	print(tables_to_delete)
if len(tables_to_create) > 0:
	print("- - - - - - - - - - - - - - - - - - - - - - - ")
	print("TO CREATE (IN SOURCE BUT NOT IN DESTINATION):")
	print(tables_to_create)
