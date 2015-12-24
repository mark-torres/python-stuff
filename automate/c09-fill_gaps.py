import re, argparse, os, shutil, sys

parser = argparse.ArgumentParser(description='Fill / open gaps in numbered files')
parser.add_argument('--dir','-d',
	dest='targetDir',
	required=True,
	nargs=1,
	help='Target directory.')
parser.add_argument('--prefix','-p',
	dest='namePrefix',
	required=True,
	nargs=1,
	help='File name prefix.')
parser.add_argument('--action','-a',
	dest='action',
	choices=['fill','open'],
	nargs=1,
	help='Gap action. If mode is set to "open", a position and gap size must be supplied. Default mode is fill.')
parser.add_argument('--pos','-s',
	dest='startPos',
	type=int,
	nargs=1,
	help='Start position to open the gap.')
parser.add_argument('--size','-n',
	dest='gapSize',
	type=int,
	nargs=1,
	help='Size of the gap.')
args = parser.parse_args()

# required args
targetDir = args.targetDir[0]
namePrefix = args.namePrefix[0]
# optional args
action = args.action[0] if (args.action != None) else 'fill'
startPos = args.startPos[0] if (args.startPos != None) else None
gapSize = args.gapSize[0] if (args.gapSize != None) else None

if action == 'open':
	if gapSize == None or startPos == None:
		print('Start position and gap size are required')
		sys.exit()

# regex
rexFiles = re.compile(r'^'+namePrefix+'(\d+)[.](\w+)')
# start
if not os.path.isdir(targetDir):
	print('Error: Target directory is not valid')
elif action == 'fill':
	files = []
	extensions = []
	numbers = []
	numSort = []
	# get files in directory
	fileList = os.listdir(targetDir)
	for fileName in fileList:
		# check if numbered
		found = rexFiles.search(fileName)
		if found != None:
			# save number
			number = int(found.group(1))
			numbers.append(number)
			numSort.append(number)
			# save file name
			files.append(fileName)
			# save file extension
			extension = found.group(2)
			extensions.append(extension)
	if len(numSort) > 1:
		numSort.sort()
		minVal = numSort[0]
		maxVal = numSort[-1]
		maxPad = len(str(maxVal))
		for i in range(0, len(numSort)):
			number = str(i + minVal)
			number = number.rjust(maxPad, '0')
			oldName = files[ numbers.index( numSort[i] ) ]
			extension = extensions[ numbers.index( numSort[i] ) ]
			newName = '%s%s.%s' % (namePrefix, number, extension)
			if newName != oldName:
				print('Renaming', oldName, '=>', newName)
				shutil.move( os.path.join(targetDir, oldName), os.path.join(targetDir, newName) )
elif action == 'open':
	files = []
	extensions = []
	numbers = []
	numSort = []
	# get files in directory
	fileList = os.listdir(targetDir)
	for fileName in fileList:
		# check if numbered
		found = rexFiles.search(fileName)
		if found != None:
			# save number
			number = int(found.group(1))
			numbers.append(number)
			numSort.append(number)
			# save file name
			files.append(fileName)
			# save file extension
			extension = found.group(2)
			extensions.append(extension)
	if len(files) > 1:
		numSort.sort()
		maxVal = numSort[-1]
		maxPad = len(str(maxVal))
		for i in range(0, len(numSort)):
			if numSort[i] > startPos:
				newNumber = numSort[i] + gapSize
				newNumber = str(newNumber)
				newNumber = newNumber.rjust(maxPad, '0')
				oldName = files[ numbers.index( numSort[i] ) ]
				extension = extensions[ numbers.index( numSort[i] ) ]
				newName = '%s%s.%s' % (namePrefix, newNumber, extension)
				print('Renaming', oldName, '=>', newName)
				shutil.move( os.path.join(targetDir, oldName), os.path.join(targetDir, newName) )
else:
	print('unknown action')
# end
