#!/usr/bin/env python3
import argparse, random, sys

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
	help="A single quoted list of column definitions (excluding primary key _ID) for the model, "+
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
javaDefinitions = {
	'INTEGER': {
		'type': "long",
		'value': "0",
		'dbFunction': "getLong"
	},
	'REAL':{
		'type': "double",
		'value': "0d",
		'dbFunction': "getDouble"
	},
	'TEXT':{
		'type': "String",
		'value': "\"\"",
		'dbFunction': "getString"
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

model = model.lower()
modelClass = class_name_str(model)
modelObj = camel_case_str(model)
modelTable = model + "s"
modelTableUpper = modelTable.upper()

print_header("model schema class", 30)

print("public final class %sSchema implements BaseColumns {" % (modelClass))
print("\tpublic static final String TABLE_NAME = \"%s\";" % (modelTable))
print("\tpublic static final String SQL_CREATE_TABLE = \"CREATE TABLE IF NOT EXISTS \" + TABLE_NAME + \" (\" +")
print("\t\t\"_ID integer PRIMARY KEY AUTOINCREMENT NOT NULL\" +")
print("\t\t\");\";")
print("\tpublic static final String SQL_EMPTY_TABLE = \"DELETE FROM \" + TABLE_NAME;")

print("\t// Columns names")
for column in colDefs.keys():
	print("\tpublic static final String COLUMN_NAME_%s = \"%s\";" % (column.upper(), column))

print("\t// Column definitions")
print("\tpublic static final HashMap<String, String> COL_DEFS;")
print("\tstatic {")
print("\t\tCOL_DEFS = new HashMap<>();")
for column in colDefs.keys():
	print("\t\tCOL_DEFS.put(COLUMN_NAME_%s, \"%s\");" % (column.upper(), colDefs[column]['type']))
print("\t}")

print("\t// Column indexes")
print("\tpublic static final HashMap<String, Boolean> COL_IDX;")
print("\tstatic {")
print("\t\tCOL_IDX = new HashMap<>();")
print("\t\tCOL_IDX.put(\"_ID\", true);")
for column in colDefs.keys():
	print("\t\tCOL_IDX.put(COLUMN_NAME_%s, %s);" % (column.upper(), 'true' if colDefs[column]['indexed'] else 'false'))
print("\t}")

print("}")
print("\n")

print_header("Model data class", 30)
print("public class %sData {" % (modelClass))
print("\tpublic long localId;")
for column in colDefs.keys():
	print("\tpublic %s %s;" % (javaDefinitions[ colDefs[column]['type'] ]['type'], camel_case_str(column)))
print("")
print("\tpublic %sData() {" % (modelClass))
print("\t\tlocalId = 0;")
for column in colDefs.keys():
	print("\t\t%s = %s;" % (camel_case_str(column), javaDefinitions[ colDefs[column]['type'] ]['value']))
print("\t}")
print("}")
print("\n")

print_header("database helper class", 30)

print("public class DbHelper extends SQLiteOpenHelper {")
print("\tpublic static final String PRIMARY_KEY_FIELD = \"_ID\";")
print("\tpublic static final int DATABASE_VERSION = 1;")
print("\tpublic static final String DATABASE_NAME = \"my_app.db\";")
print("\tprivate static ArrayList<String> dbTables;")
print("\tprivate static DbHelper instance;")
print("\n")

print("\tpublic static DbHelper getInstance(Context context) {")
print("\t\tif (instance == null) {")
print("\t\t\tinstance = new DbHelper(context.getApplicationContext());")
print("\t\t\tdbTables = new ArrayList<>();")
print("\t\t}")
print("\t\treturn instance;")
print("\t}")
print("\n")
print("\tprivate DbHelper(Context context) {")
print("\t\tsuper(context, DATABASE_NAME, null, DATABASE_VERSION);")
print("\t}")
print("\n")

print("\t@Override")
print("\tpublic void onCreate(SQLiteDatabase db) {")
print("\t\t// create tables")
print("\t\tdb.execSQL(%sSchema.SQL_CREATE_TABLE);" % (modelClass))
print("\t\t// complete table structure")
print("\t\tcheckTableStructure(db, %sSchema.TABLE_NAME, %sSchema.COL_DEFS, %sSchema.COL_IDX);" % (modelClass, modelClass, modelClass))
print("\t}")
print("\n")

print("\t@Override")
print("\tpublic void onUpgrade(SQLiteDatabase db, int oldVersion, int newVersion) {")
print("\t\t// create tables")
print("\t\tdb.execSQL(%sSchema.SQL_CREATE_TABLE);" % (modelClass))
print("\t\t// check table structure")
print("\t\tcheckTableStructure(db, %sSchema.TABLE_NAME, %sSchema.COL_DEFS, %sSchema.COL_IDX);" % (modelClass, modelClass, modelClass))
print("\t}")
print("\n")

print("\tprivate void checkTableStructure(SQLiteDatabase db, String tableName, HashMap<String, String> tableColumns, HashMap<String, Boolean> tableIndexes) {")
print("\t\t// Get columns")
print("\t\tArrayList<String> currentColumns = new ArrayList<>();")
print("\t\tString tableQuery = \"PRAGMA table_info(\" + tableName + \")\";")
print("\t\tCursor cursorTable = db.rawQuery(tableQuery, null);")
print("\t\twhile(cursorTable.moveToNext()) {")
print("\t\t\tString columnName = cursorTable.getString(cursorTable.getColumnIndex(\"name\"));")
print("\t\t\tcurrentColumns.add(columnName);")
print("\t\t}")
print("\t\tcursorTable.close();")
print("\t\t// Compare to required columns")
print("\t\tfor(String column: tableColumns.keySet()) {")
print("\t\t\tif(!currentColumns.contains(column)) {")
print("\t\t\t\t// add column if not in table")
print("\t\t\t\tString query = \"ALTER TABLE \" + tableName + \" ADD \" + column + \" \" + tableColumns.get(column) + \";\";")
print("\t\t\t\tdb.execSQL(query);")
print("\t\t\t}")
print("\t\t}")
print("\t\t// Get indexes")
print("\t\tString indexQuery = \"SELECT name FROM sqlite_master WHERE type = 'index' AND tbl_name = '\" + tableName + \"';\";")
print("\t\tCursor cursorIndex = db.rawQuery(indexQuery, null);")
print("\t\tArrayList<String> currentIndexes = new ArrayList<>();")
print("\t\twhile (cursorIndex.moveToNext()) {")
print("\t\t\tString indexName = cursorIndex.getString(cursorIndex.getColumnIndex(\"name\"));")
print("\t\t\tcurrentIndexes.add(indexName);")
print("\t\t}")
print("\t\tcursorIndex.close();")
print("\t\t// Compare to required indexes")
print("\t\tfor (String colName: tableIndexes.keySet()) {")
print("\t\t\tString indexName = tableName + \"_\" + colName;")
print("\t\t\tif (tableIndexes.get(colName) && !currentIndexes.contains(indexName)) {")
print("\t\t\t\t// add if not exists")
print("\t\t\t\tString sql = \"CREATE INDEX IF NOT EXISTS \" + indexName + \" ON \" + tableName + \" (\" + colName + \" ASC);\";")
print("\t\t\t\tdb.execSQL(sql);")
print("\t\t\t}")
print("\t\t}")
print("\t}")
print("\n")

print("\tpublic void loadDatabaseTables() {")
print("\t\tSQLiteDatabase readDb = getReadableDatabase();")
print("\t\tif (dbTables != null && dbTables.size() == 0) {")
print("\t\t\t// Load the table list")
print("\t\t\tString query = \"SELECT name FROM sqlite_master WHERE type = 'table'\";")
print("\t\t\tCursor cursor = readDb.rawQuery(query, null);")
print("\t\t\twhile (cursor.moveToNext()) {")
print("\t\t\t\tString tableName = cursor.getString(cursor.getColumnIndex(\"name\"));")
print("\t\t\t\tif (!tableName.isEmpty() && !dbTables.contains(tableName)) {")
print("\t\t\t\t\tdbTables.add(tableName);")
print("\t\t\t\t}")
print("\t\t\t}")
print("\t\t\tcursor.close();")
print("\t\t}")
print("\t\treadDb.close();")
print("\t}")
print("\n")

print("\tprivate boolean tableExists(@NonNull String tableName) {")
print("\t\treturn dbTables.contains(tableName);")
print("\t}")
print("\n")

print_header("%s OPERATIONS" % (modelTableUpper), 30)

print("\tpublic ArrayList<%sData> get%ss() {" % (modelClass, modelClass))
print("\t\tArrayList<%sData> %ss = new ArrayList<>();" % (modelClass, modelObj))
print("\t\t//if (!tableExists(%sSchema.TABLE_NAME)) return %ss;" % (modelClass, modelObj))
print("\t\tSQLiteDatabase readDb = getReadableDatabase();")
print("\t\tCursor cursor = readDb.query(%sSchema.TABLE_NAME," % (modelClass))
print("\t\t\t\tnull, // The columns to return, null for all columns")
print("\t\t\t\tnull, // The columns for the WHERE clause")
print("\t\t\t\tnull, // The values for the WHERE clause")
print("\t\t\t\tnull, // don't group the rows")
print("\t\t\t\tnull, // don't filter by row groups")
print("\t\t\t\tnull  // The SORT BY string")
print("\t\t);")
print("\t\twhile (cursor.moveToNext()) {")
print("\t\t\t%sData %s = new %sData();" % (modelClass, modelObj, modelClass))
print("\t\t\t%s.localId = cursor.getLong(cursor.getColumnIndex(PRIMARY_KEY_FIELD));" % (modelObj))
for column in colDefs.keys():
	print("\t\t\t%s.%s = cursor.%s(cursor.getColumnIndex(%sSchema.COLUMN_NAME_%s));" % 
	(modelObj, camel_case_str(column), javaDefinitions[ colDefs[column]['type'] ]['dbFunction'], modelClass, column.upper()) )
print("\t\t\t%ss.add(%s);" % (modelObj, modelObj))
print("\t\t}")
print("\t\tcursor.close();")
print("\t\treadDb.close();")
print("\t\treturn %ss;" % (modelObj))
print("\t}")
print("\n")

print("\tpublic %sData get%s(long localId) {" % (modelClass, modelClass))
print("\t\t%sData %s = new %sData();" % (modelClass, modelObj, modelClass))
print("\t\t//if (!tableExists(%sSchema.TABLE_NAME)) return %s;" % (modelClass, modelObj))
print("\t\tSQLiteDatabase readDb = getReadableDatabase();")
print("\t\tCursor cursor = readDb.query(%sSchema.TABLE_NAME," % (modelClass))
print("\t\t\t\tnull, // The columns to return, null for all columns")
print("\t\t\t\tPRIMARY_KEY_FIELD + \" = ?\", // The columns for the WHERE clause")
print("\t\t\t\tnew String[]{Long.toString(localId)}, // The values for the WHERE clause")
print("\t\t\t\tnull, // don't group the rows")
print("\t\t\t\tnull, // don't filter by row groups")
print("\t\t\t\tnull  // The SORT BY string")
print("\t\t);")
print("\t\tif (cursor.moveToFirst()) {")
print("\t\t\t%s.localId = cursor.getLong(cursor.getColumnIndex(PRIMARY_KEY_FIELD));" % (modelObj))
for column in colDefs.keys():
	print("\t\t\t%s.%s = cursor.%s(cursor.getColumnIndex(%sSchema.COLUMN_NAME_%s));" % 
	(modelObj, camel_case_str(column), javaDefinitions[ colDefs[column]['type'] ]['dbFunction'], modelClass, column.upper()) )
print("\t\t}")
print("\t\tcursor.close();")
print("\t\treadDb.close();")
print("\t\treturn %s;" % (modelObj))
print("\t}")
print("\n")

print("\tpublic long save%s(%sData %s) {" % (modelClass, modelClass, modelObj))
print("\t\tlong localId = 0L;")
print("\t\t//if (!tableExists(%sSchema.TABLE_NAME)) return localId;" % (modelClass))
print("\t\tSQLiteDatabase writeDb = getWritableDatabase();")
print("\t\tContentValues values = new ContentValues();")
for column in colDefs.keys():
	print("\t\tvalues.put(%sSchema.COLUMN_NAME_%s, %s.%s);" % (modelClass, column.upper(), modelObj, camel_case_str(column)))
print("\t\tif (%s.localId == 0L) {" % (modelObj))
print("\t\t\tlocalId = writeDb.insert(%sSchema.TABLE_NAME, null, values);" % (modelClass))
print("\t\t} else {")
print("\t\t\tlocalId = %s.localId;" % (modelObj))
print("\t\t\tint affectedRows = writeDb.update(")
print("\t\t\t\t%sSchema.TABLE_NAME," % (modelClass))
print("\t\t\t\tvalues,")
print("\t\t\t\tPRIMARY_KEY_FIELD + \" = ?\",")
print("\t\t\t\tnew String[]{Long.toString(%s.localId)}" % (modelObj))
print("\t\t\t);")
print("\t\t\tif (affectedRows == 0) {")
print("\t\t\t\tlocalId = 0L;")
print("\t\t\t}")
print("\t\t}")
print("\t\twriteDb.close();")
print("\t\treturn localId;")
print("\t}")
print("\n")

print("\tpublic boolean delete%s(long localId) {" % (modelClass))
print("\t\t//if (!tableExists(%sSchema.TABLE_NAME)) return false;" % (modelClass))
print("\t\tSQLiteDatabase writeDb = getWritableDatabase();")
print("\t\tint deletedRows = writeDb.delete(")
print("\t\t\t%sSchema.TABLE_NAME," % (modelClass))
print("\t\t\tPRIMARY_KEY_FIELD + \" = ?\",")
print("\t\t\tnew String[]{Long.toString(localId)}")
print("\t\t);")
print("\t\twriteDb.close();")
print("\t\treturn (deletedRows > 0);")
print("\t}")
# print("\n")
print("}")
print("\n")