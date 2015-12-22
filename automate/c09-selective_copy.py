import shutil, os, argparse

parser = argparse.ArgumentParser(description='Selective file type copy.')
parser.add_argument('--src', dest='sourceDir', required=True, nargs=1, help='Source directory')
parser.add_argument('--ext', dest='fileExt', required=True, nargs=1, help='File type extension (pdf, jpg, gif, etc)')
parser.add_argument('--dst', dest='destDir', required=True, nargs=1, help='Destination directory')

args = parser.parse_args()

sourceDir = args.sourceDir[0]
destDir = args.destDir[0]
fileExt = args.fileExt[0]

# validate directories
if os.path.isdir(sourceDir) and os.path.isdir(destDir):
	# walk the directory tree
	for folder, subFolders, fileNames in os.walk(sourceDir):
		for fileName in fileNames:
			if fileName.endswith('.'+fileExt):
				filePath = os.path.join(folder, fileName)
				newPath = os.path.join(destDir, fileName)
				if not os.path.isfile(newPath):
					print('Copying file:', filePath, 'to', newPath)
					shutil.copy(filePath, newPath)
				else:
					print('Skipping file:', filePath, ',', fileName, 'already exists in', destDir)
else:
	print('Error:')
	if not os.path.isdir(sourceDir):
		print('- Source directory is not a valid directory')
	if not os.path.isdir(destDir):
		print('- Destination directory is not a valid directory')
