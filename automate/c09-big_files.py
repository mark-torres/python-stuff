import os, argparse

parser = argparse.ArgumentParser(description='Find and optionally remove big files.')
parser.add_argument('--dir', dest='targetDir', required=True, nargs=1, help='Target directory')
parser.add_argument('--ext', dest='fileExt', nargs='*', help='File type extension(s) (tmp, log, mov, etc)')
parser.add_argument('--size', dest='maxSize', default=100, type=int, nargs=1, help='Maximum file size in MB')
parser.add_argument('--mode', dest='scanMode', default='list', choices=['list','delete'], nargs=1, help='Scan mode')

args = parser.parse_args()

targetDir = args.targetDir[0]
fileExt = args.fileExt
maxSize = args.maxSize[0]
scanMode = args.scanMode[0]

if not os.path.isdir(targetDir):
	print('Target directory is not valid.')
else:
	for folder, subFolders, fileNames in os.walk(targetDir):
		for fileName in fileNames:
			filePath = os.path.abspath(os.path.join(folder, fileName))
			fileSize = round( os.path.getsize(filePath) / 1024 / 1024, 1)
			bigFile = (fileSize >= maxSize)
			typeMatch = True
			# check if extensions are set
			if fileExt != None:
				typeMatch = False
				for ext in fileExt:
					if fileName.endswith(ext):
						typeMatch = True
			if bigFile and typeMatch:
				if scanMode == 'delete':
					print('Deleting file:', filePath)
					#os.unlink(filePath)
				else:
					print(str(fileSize).rjust(8), 'MB -', filePath)
