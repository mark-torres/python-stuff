#!/usr/bin/env python3
import openpyxl, sys, os, argparse, csv

parser = argparse.ArgumentParser(description = "Batch Excel to CSV converter")
parser.add_argument("--prefix", "-p",
	dest = "namePrefix",
	nargs = 1,
	help = "Filename prefix of files to convert")
parser.add_argument("--dir", "-d",
	dest = "xlsDir",
	nargs = 1,
	help = "Directory with Excel files to convert")
args = parser.parse_args()

namePrefix = args.namePrefix[0] if args.namePrefix != None else None
xlsDir = args.xlsDir[0] if args.xlsDir != None else None

# functions
def xlsx2csv(xlsxFilePath):
	try:
		workBook = openpyxl.load_workbook(xlsxFilePath)
	except:
		print("\tError reading file: %s" % (sys.exc_info()[0]))
		return False
	sheetNames = workBook.get_sheet_names()
	xlsxFileName = os.path.basename( os.path.splitext(xlsxFilePath)[0] )
	for i, sheetName in enumerate(sheetNames):
		sheet = workBook.get_sheet_by_name(sheetName)
		if not sheetName.isalnum():
			sheetName = "Sheet%d" % (i + 1)
		csvFileName = "%s[%s].csv" % (xlsxFileName, sheetName.strip())
		csvFilePath = os.path.join(os.path.dirname(xlsxFilePath), csvFileName)
		print("\tWriting '%s'" % (csvFilePath))
		try:
			csvFile = open(csvFilePath, 'w', newline='')
		except:
			print("\t\tError creating file")
			break
		csvWriter = csv.writer(csvFile)
		# write rows
		for xlsRow in sheet.rows:
			csvRow = []
			for xlsCell in xlsRow:
				csvRow.append(xlsCell.value)
			csvWriter.writerow(csvRow)
		csvFile.close()
	return True

# check directory
if xlsDir != None and not os.path.isdir(xlsDir):
	print("Error: %s is not a directory")
	sys.exit()
elif xlsDir == None:
	xlsDir = os.getcwd()

# process files
for fileName in os.listdir(xlsDir):
	if not os.path.isdir(fileName) and fileName.endswith(".xlsx"):
		processFile = True
		if namePrefix != None and not fileName.startswith(namePrefix):
			processFile = False
		if processFile:
			print("Processing file: %s" % (fileName))
			if xlsx2csv(os.path.join(xlsDir, fileName)):
				print("\tOK")
			else:
				print("\tFAILED")
