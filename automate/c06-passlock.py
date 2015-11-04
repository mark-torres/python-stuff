#! /usr/local/bin/python3

# =======================================
# = AN INSECURE PASSWORD LOCKER PROGRAM =
# =======================================

import sys, pyperclip, configparser
# if pyperclip is not installed, install with: pip3 install pyperclip

def showUsage():
	print('Usage: ', sys.argv[0], ' [account]')

if len(sys.argv[1:]) > 0:
	account = sys.argv[1]
else:
	print('No account specified')
	showUsage()
	sys.exit()

# read accounts data file
dataFile = "./passlock.ini"

config = configparser.ConfigParser()
config.read(dataFile)
if not 'accounts' in config:
	print('Error reading accounts data')
	sys.exit()

if account in config['accounts']:
	pyperclip.copy(config['accounts'][account])
	print('Password for',account,'copied to the clipboard')
else:
	print('Account "'+ account+'" not found. Available accounts:')
	for acc in config['accounts']:
		print('*',acc)
