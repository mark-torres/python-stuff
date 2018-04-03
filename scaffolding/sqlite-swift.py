#!/usr/bin/env python3
import argparse, random, sys

# ====================
# = ARGUMENTS PARSER =
# ====================

parser = argparse.ArgumentParser(description='Generates code to manage SQLite databases with SQLite.swift wrapper.')

parser.add_argument('--model','-m',
	dest='model',
	required=True,
	nargs=1,
	help="Singularized model name. (e.g. 'app_user' not 'app_users')")

parser.add_argument('--columns','-c',
	dest='columns',
	required=True,
	nargs=1,
	help="A single quoted list of column definitions (excluding primary key column) for the model, "+
	"separated by semicolon. Valid types are: integer, real, text. Indexed columns can be "+
	"indicated by adding 'i' to definition. Example: 'name:text;weight:real;profile_id:integer:i'")

args = parser.parse_args()

model = args.model[0]
columns = args.columns[0]

# =============
# = FUNCTIONS =
# =============
def parse_columns(colsString):
	"""Parse column definitions"""
	definitions = {}
	columns = colsString.split(';')
	for i in range( len(columns) ):
		column = columns[i].strip()
		parts = column.split(':')
		indexed = False
		if(len(parts) == 3 and parts[2] == "i"):
			indexed = True
		definitions[ parts[0] ] = {'type': parts[1].upper(), 'indexed': indexed}
	return definitions
	
def camel_case_str(planeString):
	"""Get the camel case version of a string"""
	planeString = planeString.lower()
	parts = planeString.split("_")
	if(len(parts) == 1):
		return planeString
	else:
		for i in range( len(parts) ):
			if(i > 0):
				parts[i] = parts[i].title()
		return "".join(parts)

def class_name_str(planeString):
	"""Get the title case version of a string"""
	planeString = planeString.lower()
	parts = planeString.split("_")
	for i in range( len(parts) ):
		parts[i] = parts[i].title()
	return "".join(parts)

def print_header(title, size):
	title = title.strip()
	title = title.upper()
	print("// " + " ".rjust(25, "*") + title.center(size, " ") + " ".ljust(25,"*"))
	print("")

validDataTypes = ["INTEGER","REAL","TEXT"]

swiftDefinitions = {
	'INTEGER': {
		'type': "Int",
		'value': "0"
	},
	'REAL':{
		'type': "Double",
		'value': "0"
	},
	'TEXT':{
		'type': "String",
		'value': "\"\""
	}
}

# ==================
# = IMPLEMENTATION =
# ==================
colDefs = parse_columns(columns)

# validate column types
colTypesValid = True
indexedColumns = []
for column in colDefs.keys():
	if(colDefs[column]['indexed']):
		indexedColumns.append(column)
	colType = colDefs[column]['type']
	if colType not in validDataTypes:
		colTypesValid = False

if not colTypesValid:
	print("Please use valid data types.")
	sys.exit()

model = model.lower()                # e.g. my_model
modelClass = class_name_str(model)   # e.g. MyModel
modelObj = camel_case_str(model)     # e.g. myModel
modelTable = model + "s"             # e.g. my_models
modelTableUpper = modelTable.upper() # e.g. MY_MODELS

# ==========
# = OUTPUT =
# ==========

print_header("content for DBManager file, copy just necessary code", 60)

print("import Foundation")
print("import SQLite")

print("\n")

print("struct DBTables {")
print("\tstatic let %s = \"%s\"" % (class_name_str(modelTable), modelTable) )
print("}")

print("\n")

print("let primaryColumnName = \"row_id\"")

print("\n")

print("class DBManager {")
print("\n\tvar db: Connection")
print("\n\tenum ColumnType {")
print("\t\tcase integer")
print("\t\tcase text")
print("\t\tcase real")
print("\t}")
print("\n\tstruct ColumnDefinition {")
print("\t\tvar name: String")
print("\t\tvar type: ColumnType")
print("\t\t")
print("\t\tinit(_ name: String, _ type: ColumnType) {")
print("\t\t\tself.name = name")
print("\t\t\tself.type = type")
print("\t\t}")
print("\t}")
print("\n\tinit(dbPath path: String) {")
print("\t\tdb = try! Connection(path)")
print("\t}")
print("\n\tfunc initTable(_ table: Table) -> Bool {")
print("\t\tlet rowId = Expression<Int64>(primaryColumnName)")
print("\t\tdo {")
print("\t\t\ttry db.run(table.create(temporary: false, ifNotExists: true, withoutRowid: false, block: { (tb) in")
print("\t\t\t\ttb.column(rowId, primaryKey: PrimaryKey.autoincrement)")
print("\t\t\t}) )")
print("\t\t} catch (let error) {")
print("\t\t\tprint(error.localizedDescription)")
print("\t\t\treturn false")
print("\t\t}")
print("\t\treturn true")
print("\t}")
print("\n\tfunc completeTable(_ tableName: String, withColumns columns: [ColumnDefinition]) -> Bool {")
print("\t\tvar query = \"\"")
print("\t\tlet table = Table(tableName)")
print("\t\tlet currentColumns = getColumnNames(fromTable: tableName)")
print("\t\tfor col in columns {")
print("\t\t\tif !currentColumns.contains(col.name) {")
print("\t\t\t\tswitch col.type {")
print("\t\t\t\tcase ColumnType.integer:")
print("\t\t\t\t\tlet c = Expression<Int64>(col.name)")
print("\t\t\t\t\tquery = table.addColumn(c, defaultValue: 0)")
print("\t\t\t\t\tbreak")
print("\t\t\t\tcase ColumnType.real:")
print("\t\t\t\t\tlet c = Expression<Double>(col.name)")
print("\t\t\t\t\tquery = table.addColumn(c, defaultValue: 0.0)")
print("\t\t\t\t\tbreak")
print("\t\t\t\tdefault:")
print("\t\t\t\t\tlet c = Expression<String>(col.name)")
print("\t\t\t\t\tquery = table.addColumn(c, defaultValue: \" \")")
print("\t\t\t\t}")
print("\t\t\t\tdo {")
print("\t\t\t\t\ttry db.run(query)")
print("\t\t\t\t} catch (let error) {")
print("\t\t\t\t\tprint(error.localizedDescription)")
print("\t\t\t\t}")
print("\t\t\t}")
print("\t\t}")
print("\t\treturn true")
print("\t}")
print("\n\tfunc getColumnNames(fromTable tableName: String) -> [String] {")
print("\t\tvar columnNames = [String]()")
print("\t\tguard let rows = try? db.prepare(\"PRAGMA table_info(\" + tableName + \")\") else {")
print("\t\t\tprint(\"Error getting table columns from \" + tableName)")
print("\t\t\treturn columnNames")
print("\t\t}")
print("\t\tfor row in rows {")
print("\t\t\tif let colName = row[1] as? String {")
print("\t\t\t\tcolumnNames.append(colName)")
print("\t\t\t}")
print("\t\t}")
print("\t\treturn columnNames")
print("\t}")
print("\n\tfunc addIndexToTable(_ table: Table, forColumn column: ColumnDefinition) -> Bool {")
print("\t\tvar query = \"\"")
print("\t\tswitch column.type {")
print("\t\tcase ColumnType.integer:")
print("\t\t\tlet col = Expression<Int64>(column.name)")
print("\t\t\tquery = table.createIndex(col, unique: false, ifNotExists: true)")
print("\t\tcase ColumnType.real:")
print("\t\t\tlet col = Expression<Double>(column.name)")
print("\t\t\tquery = table.createIndex(col, unique: false, ifNotExists: true)")
print("\t\tdefault:")
print("\t\t\tlet col = Expression<String>(column.name)")
print("\t\t\tquery = table.createIndex(col, unique: false, ifNotExists: true)")
print("\t\t}")
print("\t\tdo {")
print("\t\t\ttry db.run(query)")
print("\t\t} catch (let error) {")
print("\t\t\tprint(error.localizedDescription)")
print("\t\t\treturn false")
print("\t\t}")
print("\t\treturn true")
print("\t}")
print("}")

print("\n")

print_header("model extension file", 60)

print("import Foundation")
print("import SQLite")

print("\n")

print("class DB%sData {" % (modelClass))
print("\tvar rowId: Int64")
for column in colDefs.keys():
	colVar = camel_case_str(column)
	colType = swiftDefinitions[ colDefs[column]['type'] ]['type']
	print("\tvar %s: %s" % (colVar, colType))
print("\n\tinit() {")
print("\t\trowId = 0")
for column in colDefs.keys():
	colVar = camel_case_str(column)
	colVal = swiftDefinitions[ colDefs[column]['type'] ]['value']
	print("\t\t%s = %s" % (colVar, colVal))
print("\t}")
print("}")

print("\n")

print("struct DB%ssSchema {" % (modelClass))
print("\tstatic let table = Table(TableNames.%ss)" % (modelClass))
print("\tstatic let rowId = Expression<Int64>(primaryColumnName)")
for column in colDefs.keys():
	colVar = camel_case_str(column)
	colType = swiftDefinitions[ colDefs[column]['type'] ]['type']
	print("\tstatic let %s = Expression<%s>(\"%s\")" % (colVar, colType, column))
print("}")

print("\n")

print("extension DBManager {")
print("\n\tfunc create%ssTable() -> Bool {" % (modelClass))
print("\t\tlet table = Table(TableNames.%ss)" % (modelClass))
print("\t\t// create table")
print("\t\tguard initTable(table) else {")
print("\t\t\tprint(\"Error creating table: \" + TableNames.%ss)" % (modelClass))
print("\t\t\treturn false")
print("\t\t}")
print("\t\t// complete table")
listCols = []
for column in colDefs.keys():
	colVar = camel_case_str(column)
	listCols.append(colVar)
	colType = colDefs[column]['type'].lower()
	print("\t\tlet %s = ColumnDefinition(\"%s\", .%s)" % (colVar, column, colType))
print("\t\tlet columns: [ColumnDefinition] = [%s]" % ( ", ".join(listCols) ))
print("\t\tguard completeTable(TableNames.%ss, withColumns: columns) else {" % (modelClass))
print("\t\t\tprint(\"Error completing table: \" + TableNames.%ss)" % (modelClass))
print("\t\t\treturn false")
print("\t\t}")
print("\t\t// add indexes")
for column in colDefs.keys():
	if colDefs[column]['indexed']:
		colVar = camel_case_str(column)
		print("\t\tif !addIndexToTable(table, forColumn: %s) {" % (colVar))
		print("\t\t\tprint(\"Error adding index for column \(%s.name) to table \" + TableNames.%ss)" % (colVar, modelClass))
		print("\t\t}")
print("\t\treturn true")
print("\t}")
print("\n\tfunc getAll%ss() -> [DB%sData] {" % (modelClass, modelClass))
print("\t\tvar %ss = [DB%sData]()" % (modelObj, modelClass))
print("\t\tguard let rows = try? db.prepare(DB%ssSchema.table) else {" % (modelClass))
print("\t\t\tprint(\"getAll%ss: Error getting data from table: \" + TableNames.%ss)" % (modelClass, modelClass))
print("\t\t\treturn %ss" % (modelObj))
print("\t\t}")
print("\t\tfor row in rows {")
print("\t\t\tlet %s = DB%sData()" % (modelObj, modelClass))
print("\t\t\t%s.rowId = row[DB%ssSchema.rowId]" % (modelObj, modelClass))
for column in colDefs.keys():
	colVar = camel_case_str(column)
	print("\t\t\t%s.%s = row[DB%ssSchema.%s]" % (modelObj, colVar, modelClass, colVar))
print("\t\t\t%ss.append(%s)" % (modelObj, modelObj))
print("\t\t}")
print("\t\treturn %ss" % (modelObj))
print("\t}")
print("\n\tfunc get%s(byId rowId: Int64) -> DB%sData {" % (modelClass, modelClass))
print("\t\tvar %s = DB%sData()" % (modelObj, modelClass))
print("\t\tguard let rows = try? db.prepare(DB%ssSchema.table.filter(DB%ssSchema.rowId == rowId).limit(1)) else {" % (modelClass, modelClass))
print("\t\t\tprint(\"get%s: Error getting data from table: \" + TableNames.%ss)" % (modelClass, modelClass))
print("\t\t\treturn %s" % (modelObj))
print("\t\t}")
print("\t\tfor row in rows {")
print("\t\t\t%s.rowId = row[DB%ssSchema.rowId]" % (modelObj, modelClass))
for column in colDefs.keys():
	colVar = camel_case_str(column)
	print("\t\t\t%s.%s = row[DB%ssSchema.name]" % (modelObj, colVar, modelClass))
print("\t\t}")
print("\t\treturn %s" % (modelObj))
print("\t}")
print("\n\tfunc save%s(_ %s: DB%sData) -> Int64 {" % (modelClass, modelObj, modelClass))
print("\t\tif %s.rowId == 0 {" % (modelObj))
print("\t\t\t// insert")
print("\t\t\tlet insert = DB%ssSchema.table.insert(" % (modelClass))
for column in colDefs.keys():
	colVar = camel_case_str(column)
	print("\t\t\t\tDB%ssSchema.%s <- %s.%s," % (modelClass, colVar, modelObj, colVar))
print("\t\t\t)")
print("\t\t\tguard let newRowId = try? db.run(insert) else {")
print("\t\t\t\tprint(\"save%s: Error inserting row\")" % (modelClass))
print("\t\t\t\treturn 0")
print("\t\t\t}")
print("\t\t\treturn newRowId")
print("\t\t} else {")
print("\t\t\t// update")
print("\t\t\tlet update = DB%ssSchema.table.where(DB%ssSchema.rowId == %s.rowId).update(" % (modelClass, modelClass, modelObj))
for column in colDefs.keys():
	colVar = camel_case_str(column)
	print("\t\t\t\tDB%ssSchema.%s <- %s.%s," % (modelClass, colVar, modelObj, colVar))
print("\t\t\t)")
print("\t\t\tguard let updatedRows = try? db.run(update) else {")
print("\t\t\t\tprint(\"save%s: Error updating row\")" % (modelClass))
print("\t\t\t\treturn 0")
print("\t\t\t}")
print("\t\t\treturn (updatedRows > 0) ? %s.rowId : 0" % (modelObj))
print("\t\t}")
print("\t}")
print("\n\tfunc delete%s(byId rowId: Int64) -> Bool {" % (modelClass))
print("\t\tlet delete = DB%ssSchema.table.where(DB%ssSchema.rowId == rowId).delete()" % (modelClass, modelClass))
print("\t\tguard let deletedRows = try? db.run(delete) else {")
print("\t\t\tprint(\"delete%s: Error deleting row\")" % (modelClass))
print("\t\t\treturn false")
print("\t\t}")
print("\t\treturn deletedRows > 0")
print("\t}")
print("}")

print("\n")
