#!/usr/bin/env python
import sys, os

if len(sys.argv) > 1:
	filesDir = sys.argv[1]
	if os.path.isdir(filesDir):
		for folderName, subfolders, filenames in os.walk(filesDir):
			print('')
			print('### Folder `%s`' % (folderName))
			print('')
			for filename in filenames:
				if not filename.startswith("."):
					print('**`%s`**' % (filename))
					print('')
					print('*Description*: File description.')
					print('')
					print('*Access*: Access method.')
					print('')
