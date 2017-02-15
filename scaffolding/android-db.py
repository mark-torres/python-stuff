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

parser.add_argument('--columns','-c',
	dest='columns',
	required=True,
	nargs=1,
	help="A single quoted list of column definitions (excluding primary key _ID) for the model, separated by semicolon. Example: 'name:varchar(100);age:smallint;weight:decimal(4,2)'")

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
	print("")

# ==================
# = IMPLEMENTATION =
# ==================
colDefs = parse_columns(columns)
indexedColumns = []
for column in colDefs.keys():
	if(colDefs[column]['indexed']):
		indexedColumns.append(column)

model = model.lower()
modelClass = class_name_str(model)
modelObj = camel_case_str(model)
modelTable = model + "s"
modelTableUpper = modelTable.upper()

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
for column in colDefs.keys():
	print("\t\tpublic static final String COLUMN_NAME_%s = \"%s\";" % (column.upper(), column))

print("\t\t// Column definitions")
print("\t\tpublic static final HashMap<String, String> COL_DEFS;")
print("\t\tstatic {")
print("\t\t\tCOL_DEFS = new HashMap<>();")
for column in colDefs.keys():
	print("\t\t\tCOL_DEFS.put(COLUMN_NAME_%s, \"%s\");" % (column.upper(), colDefs[column]['type']))
print("\t\t}")

print("\t\t// Column indexes")
print("\t\tpublic static final HashMap<String, Boolean> COL_IDX;")
print("\t\tstatic {")
print("\t\t\tCOL_IDX = new HashMap<>();")
print("\t\t\tCOL_IDX.put(\"_ID\", true);")
for column in colDefs.keys():
	print("\t\t\tCOL_IDX.put(COLUMN_NAME_%s, %s);" % (column.upper(), 'true' if colDefs[column]['indexed'] else 'false'))
print("\t\t}")

print("\t}")
print("}")
print("\n")

print_header("Model data class", 30)
print("public class %sData {" % (modelClass))
print("\tpublic long localId;")
for column in colDefs.keys():
	print("\tpublic String %s;" % (camel_case_str(column)))
print("")
print("\tpublic %sData() {" % (modelClass))
print("\t\tlocalId = 0;")
for column in colDefs.keys():
	print("\t\t%s = \"\";" % (camel_case_str(column)))
print("\t}")
print("}")
print("\n")

print_header("helper methods", 30)
print("private void checkTableStructure(SQLiteDatabase db, String tableName, HashMap<String, String> tableColumns, HashMap<String, Boolean> tableIndexes) {")
print("\t// Get columns")
print("\tArrayList<String> currentColumns = new ArrayList<>();")
print("\tString tableQuery = \"PRAGMA table_info(\" + tableName + \")\";")
# print("\tif (inDebugMode) System.out.println(tableQuery);")
print("\tCursor cursorTable = db.rawQuery(tableQuery, null);")
print("\twhile(cursorTable.moveToNext()) {")
print("\t\tString columnName = cursorTable.getString(cursorTable.getColumnIndex(\"name\"));")
print("\t\tcurrentColumns.add(columnName);")
print("\t}")
print("\tcursorTable.close();")
print("\t// Compare to required columns")
print("\tfor(String column: tableColumns.keySet()) {")
print("\t\tif(!currentColumns.contains(column)) {")
print("\t\t\t// add column if not in table")
print("\t\t\tString query = \"ALTER TABLE \" + tableName + \" ADD \" + column + \" \" + tableColumns.get(column) + \";\";")
# print("\t\t\tif (inDebugMode) System.out.println(query);")
print("\t\t\tdb.execSQL(query);")
print("\t\t}")
print("\t}")
print("\t// Get indexes")
print("\tString indexQuery = \"SELECT name FROM sqlite_master WHERE type = 'index' AND tbl_name = '\" + tableName + \"';\";")
# print("\tif (inDebugMode) System.out.println(indexQuery);")
print("\tCursor cursorIndex = db.rawQuery(indexQuery, null);")
print("\tArrayList<String> currentIndexes = new ArrayList<>();")
print("\twhile (cursorIndex.moveToNext()) {")
print("\t\tString indexName = cursorIndex.getString(cursorIndex.getColumnIndex(\"name\"));")
print("\t\tcurrentIndexes.add(indexName);")
print("\t}")
print("\tcursorIndex.close();")
print("\t// Compare to required indexes")
print("\tfor (String colName: tableIndexes.keySet()) {")
print("\t\tString indexName = tableName + \"_\" + colName;")
print("\t\tif (tableIndexes.get(colName) && !currentIndexes.contains(indexName)) {")
print("\t\t\t// add if not exists")
print("\t\t\tString sql = \"CREATE INDEX IF NOT EXISTS \" + indexName + \" ON \" + tableName + \" (\" + colName + \" ASC);\";")
# print("\t\t\tif (inDebugMode) System.out.println(sql);")
print("\t\t\tdb.execSQL(sql);")
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
print("\n")

print_header("DB OPERATIONS (DB HELPER METHODS)", 30)

print("private ArrayList<%sData> get%ss() {" % (modelClass, modelClass))
print("\tArrayList<%sData> %ss = new ArrayList<>();" % (modelClass, modelObj))
print("\tSQLiteDatabase readDb = getReadableDatabase();")
print("\tCursor cursor = readDb.query(OwnerSchema.TABLE_NAME,")
print("\t\t\tnull, // The columns to return, null for all columns")
print("\t\t\tnull, // The columns for the WHERE clause")
print("\t\t\tnull, // The values for the WHERE clause")
print("\t\t\tnull, // don't group the rows")
print("\t\t\tnull, // don't filter by row groups")
print("\t\t\tnull  // The SORT BY string")
print("\t);")
print("\twhile (cursor.moveToNext()) {")
print("\t\t%sData %s = new %sData();" % (modelClass, modelObj, modelClass))
print("\t\t%s.localId = cursor.getLong(cursor.getColumnIndex(PRIMARY_KEY_FIELD));" % (modelObj))
for column in colDefs.keys():
	print("\t\t%s.%s = cursor.getString(cursor.getColumnIndex(%sSchema.COLUMN_NAME_%s));" % (modelObj, camel_case_str(column), modelClass, column.upper()))
print("\t\t%ss.add(%s);" % (modelObj, modelObj))
print("\t}")
print("\tcursor.close();")
print("\treadDb.close();")
print("\treturn %ss;" % (modelObj))
print("}")
print("\n")

print("private %sData get%s(long localId) {" % (modelClass, modelClass))
print("\t%sData %s = new %sData();" % (modelClass, modelObj, modelClass))
print("\tSQLiteDatabase readDb = getReadableDatabase();")
print("\tCursor cursor = readDb.query(OwnerSchema.TABLE_NAME,")
print("\t\t\tnull, // The columns to return, null for all columns")
print("\t\t\tPRIMARY_KEY_FIELD + \" = ?\", // The columns for the WHERE clause")
print("\t\t\tnew String[]{Long.toString(localId)}, // The values for the WHERE clause")
print("\t\t\tnull, // don't group the rows")
print("\t\t\tnull, // don't filter by row groups")
print("\t\t\tnull  // The SORT BY string")
print("\t);")
print("\tif (cursor.moveToNext()) {")
print("\t\t%s.localId = cursor.getLong(cursor.getColumnIndex(PRIMARY_KEY_FIELD));" % (modelObj))
for column in colDefs.keys():
	print("\t\t%s.%s = cursor.getString(cursor.getColumnIndex(%sSchema.COLUMN_NAME_%s));" % (modelObj, camel_case_str(column), modelClass, column.upper()))
print("\t}")
print("\tcursor.close();")
print("\treadDb.close();")
print("\treturn %s;" % (modelObj))
print("}")
print("\n")

print("private long save%s(%sData %s) {" % (modelClass, modelClass, modelObj))
print("\tlong localId = 0;")
print("\tSQLiteDatabase writeDb = getWritableDatabase();")
print("\tContentValues values = new ContentValues();")
for column in colDefs.keys():
	print("\tvalues.put(%sSchema.COLUMN_NAME_%s, %s.%s);" % (modelClass, column.upper(), modelObj, camel_case_str(column)))
print("\tlocalId = writeDb.insert(%sSchema.TABLE_NAME, null, values);" % (modelClass))
print("\twriteDb.close();")
print("\treturn localId;")
print("}")
print("\n")

# print("\n")
