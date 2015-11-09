#! /usr/local/bin/python3

import sys, os

def readAdjective():
	adj = 'ADJECTIVE'
	while adj == 'ADJECTIVE':
		adj = input('Enter an adjective: ')
	return adj

def readNoun():
	noun = 'NOUN'
	while noun == 'NOUN':
		noun = input('Enter a noun: ')
	return noun

def readAdverb():
	adv = 'ADVERB'
	while adv == 'ADVERB':
		adv = input('Enter an adverb: ')
	return adv

def readVerb():
	verb = 'VERB'
	while verb == 'VERB':
		verb = input('Enter a verb: ')
	return verb

# Check arguments
if len(sys.argv) == 2:
	filePath = sys.argv[1]
else:
	print('Text file not provided')
	sys.exit()

# Check if file exists
if not os.path.exists(filePath):
	print('File does not exist:', filePath)
	sys.exit()

try:
	textFile = open(filePath)
except OSError as e:
	print('Error opening file:', e.strerror)

lines = textFile.readlines()
textFile.close()

modLines = []

for line in lines:
	# find text
	found = True
	while found:
		found = False
		if line.find('ADJECTIVE') >= 0:
			found = True
			index = line.find('ADJECTIVE')
			length = len('ADJECTIVE')
			replacement = readAdjective()
			line = line[:index] + replacement + line[index + length:]
		if line.find('ADVERB') >= 0:
			found = True
			index = line.find('ADVERB')
			length = len('ADVERB')
			replacement = readAdverb()
			line = line[:index] + replacement + line[index + length:]
		if line.find('NOUN') >= 0:
			found = True
			index = line.find('NOUN')
			length = len('NOUN')
			replacement = readNoun()
			line = line[:index] + replacement + line[index + length:]
		if line.find('VERB') >= 0:
			found = True
			index = line.find('VERB')
			length = len('VERB')
			replacement = readVerb()
			line = line[:index] + replacement + line[index + length:]
	modLines = modLines + [line]

if len(modLines) > 0:
	# show on screen
	for line in modLines:
		print(line, end = '')
	print('')
	# save to a file
	fileDir, fileName = os.path.split(filePath)
	fileName = 'mod-' + fileName
	filePath = os.path.join(fileDir, fileName);
	try:
		modFile = open(filePath, 'w')
	except OSError as e:
		print('Error creating file', e.strerror)
		sys.exit()
	modFile.write(''.join(modLines))
	modFile.close()
else:
	print('No lines to print')

