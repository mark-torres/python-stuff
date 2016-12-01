#!/usr/bin/env python3
import argparse, random

# ====================
# = ARGUMENTS PARSER =
# ====================

parser = argparse.ArgumentParser(description='Generates Java code for SQLiteOpenHelper definitions in Android.')

parser.add_argument('--model','-m',
	dest='model',
	required=True,
	nargs=1,
	help="Model (table) name")

parser.add_argument('--fields','-f',
	dest='fields',
	required=True,
	nargs=1,
	help="A single quoted list of field definitions (excluding primary key _ID) for the model, separated by semicolon. Example: 'name:varchar(100);age:smallint;weight:decimal(4,2)'")

args = parser.parse_args()

model = args.model[0]
fields = args.fields[0]

# =============
# = FUNCTIONS =
# =============
def parse_fields(fieldsString):
	"""Parse field definitions"""
	definitions = {}
	fields = fieldsString.split(';')
	for i in range( len(fields) ):
		field = fields[i].strip()
		if(len(field.split(':')) == 2):
			fieldName, fieldType = field.split(':')
			definitions[fieldName] = fieldType.upper()
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
# ==================
# = IMPLEMENTATION =
# ==================

fieldDefs = parse_fields(fields)

modelUpper = model.upper()
fieldsVar = "COLS_%s_TABLE" % (modelUpper)
modelClass = class_name_str(model)

print_header("variable definitions", 30)
print("private static final String TBL_%s = \"%s\";" % (modelUpper, model))
print("private static final String CREATE_TBL_%s = \"CREATE TABLE IF NOT EXISTS \" + TBL_%s + \" (\" +" % (modelUpper, modelUpper))
print("\t\"_ID integer PRIMARY KEY AUTOINCREMENT NOT NULL\" +")
print("\t\");\";")
print("private static final HashMap<String, String> %s = new HashMap<>();" % (fieldsVar))
print("\n")

print_header("Structure definition", 30)
for field in fieldDefs.keys():
	print("%s.put(\"%s\", \"%s\");" % (fieldsVar, field, fieldDefs[field]))
print("\n")

print_header("helper methods", 30)
print("private void checkTableStructure(SQLiteDatabase db, String tableName, HashMap<String, String> tableFields) {")
print("\t// get table columns")
print("\tSystem.out.println(\"Checking table structure for:\" + tableName);")
print("\tArrayList<String> currentFields = new ArrayList<>();")
print("\tCursor cursorTable = db.rawQuery(\"PRAGMA table_info(\" + tableName + \")\", null);")
print("\tint iName = cursorTable.getColumnIndex(\"name\");")
print("\twhile(cursorTable.moveToNext()) {")
print("\t\tString fieldName = cursorTable.getString(iName);")
print("\t\tcurrentFields.add(fieldName);")
print("\t}")
print("\tcursorTable.close();")
print("\t// compare to required fields")
print("\tfor(String field: tableFields.keySet()) {")
print("\t\tif(!currentFields.contains(field)) {")
print("\t\t\t// add field if not in table")
print("\t\t\tSystem.out.println(\"Adding \" + field + \" field to table \" + tableName);")
print("\t\t\tString query = \"ALTER TABLE \" + tableName + \" ADD \" + field + \" \" + tableFields.get(field) + \";\";")
print("\t\t\tdb.execSQL(query);")
print("\t\t}")
print("\t}")
print("}")

print("@Override")
print("public void onCreate(SQLiteDatabase db) {")
print("\t// create tables")
print("\tdb.execSQL(CREATE_TBL_%s);" % (modelUpper))
print("\t// complete table structure")
print("\tcheckTableStructure(db, TBL_%s, %s);" % (modelUpper, fieldsVar))
print("}")

print("@Override")
print("public void onUpgrade(SQLiteDatabase db, int oldVersion, int newVersion) {")
print("\t// check table structure")
print("\tcheckTableStructure(db, TBL_%s, %s);" % (modelUpper, fieldsVar))
print("}")

# print("\n")
