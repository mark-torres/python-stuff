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
	help="Singularized model name. (e.g. 'user' not 'users')")

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
		parts = field.split(':')
		if(len(parts) == 2):
			definitions[ parts[0] ] = {'type': parts[1].upper(), 'indexed': False}
		if(len(parts) == 3 and parts[2] == "i"):
			definitions[ parts[0] ] = {'type': parts[1].upper(), 'indexed': True}
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
indexedFields = []
for field in fieldDefs.keys():
	if(fieldDefs[field]['indexed']):
		indexedFields.append(field)

print(indexedFields)

model = model.lower()
modelClass = class_name_str(model)
modelTable = model + "s"
modelTableUpper = modelTable.upper()
# fieldsVar = "COL_DEF_%s" % (modelTableUpper)
# indexesVar = "IDX_DEF_%s" % (modelTableUpper)

print_header("contract class", 30)
print("public final class MyDbContract {")
print("\t// To prevent someone from accidentally instantiating the contract class,")
print("\t// make the constructor private.")
print("\tprivate MyDbContract() {}")
print("\t/* Inner class that defines the table contents */")
print("\tpublic final class %sSchema implements BaseColumns {" % (modelClass))
print("\t\tpublic static final String TABLE_NAME = \"%s\";" % (modelTable))
print("\t\tpublic static final String SQL_CREATE_TABLE = \"CREATE TABLE IF NOT EXISTS \" + TABLE_NAME + \" (\" +")
print("\t\t\t\"_ID integer PRIMARY KEY AUTOINCREMENT NOT NULL\" +")
print("\t\t\t\");\";")
print("\t\tpublic static final String SQL_EMPTY_TABLE = \"DELETE FROM \" + TABLE_NAME;")

print("\t\t// Columns names")
for field in fieldDefs.keys():
	print("\t\tpublic static final String COLUMN_NAME_%s = \"%s\";" % (field.upper(), field))

print("\t\t// Column definitions")
print("\t\tpublic static final HashMap<String, String> COL_DEFS;")
print("\t\tstatic {")
print("\t\t\tCOL_DEFS = new HashMap<>();")
for field in fieldDefs.keys():
	print("\t\t\tCOL_DEFS.put(COLUMN_NAME_%s, \"%s\");" % (field.upper(), fieldDefs[field]['type']))
print("\t\t}")

print("\t\t// Column indexes")
print("\t\tpublic static final HashMap<String, Boolean> COL_IDX;")
print("\t\tstatic {")
print("\t\t\tCOL_IDX = new HashMap<>();")
for field in fieldDefs.keys():
	print("\t\t\tCOL_IDX.put(COLUMN_NAME_%s, %s);" % (field.upper(), 'true' if fieldDefs[field]['indexed'] else 'false'))
print("\t\t}")

print("\t}")
print("}")
print("\n")

print_header("helper methods", 30)
print("private void checkTableStructure(SQLiteDatabase db, String tableName, HashMap<String, String> tableFields, HashMap<String, Boolean> tableIndexes) {")
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
print("\tdb.execSQL(%sSchema.SQL_CREATE_TABLE);" % (modelClass))
print("\t// complete table structure")
print("\tcheckTableStructure(db, %sSchema.TABLE_NAME, %sSchema.COL_DEFS, %sSchema.COL_IDX);" % (modelClass, modelClass, modelClass))
print("}")

print("@Override")
print("public void onUpgrade(SQLiteDatabase db, int oldVersion, int newVersion) {")
print("\t// check table structure")
print("\tcheckTableStructure(db, %sSchema.TABLE_NAME, %sSchema.COL_DEFS, %sSchema.COL_IDX);" % (modelClass, modelClass, modelClass))
print("}")

# print("\n")
