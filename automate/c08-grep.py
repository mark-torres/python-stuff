#! /usr/local/bin/python3

import sys, os, re

# Check arguments
if len(sys.argv) == 3:
	regex = sys.argv[1]
	directory = sys.argv[2]
else:
	print('Simple grep-like script with Python')
	print('Usage:')
	print(sys.argv[0], 'REGEX','DIRECTORY')
	sys.exit()

# Validate directory
if (not os.path.exists(directory) or not os.path.isdir(directory)):
	print(directory,'is not a valid directory')
	sys.exit()

userRegex = re.compile(regex)
txtRegex = re.compile(r'\.txt$')
fileList = os.listdir(directory)

for filename in fileList:
	if txtRegex.search(filename) != None:
		filePath = os.path.join(directory, filename)
		try:
			file = open(filePath, 'r')
		except:
			print('Error opening file:', filePath)
			continue
		lines = file.readlines()
		file.close()
		# search in lines
		for i in range( len(lines) ):
			line = lines[i].strip()
			lineNum = i + 1
			if userRegex.search(line) != None:
				print(filePath + '['+str(lineNum)+']:',line)
