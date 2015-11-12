#!/usr/bin/env python

import sys, os, re

def getHost(textLine):
	"""Get the host and service from a line of text"""
	host = ''
	service = ''
	regexServiceHost = re.compile(r'(\w+):\s*(\d+[.]\d+([.]([*]|\d+)){2})')
	matches = regexServiceHost.match(textLine)
	if matches != None:
		service = matches.group(1)
		host = matches.group(2)
	return (service, host)

hostsAllowFile = "/etc/hosts.allow"
filesDir = "/Applications/XAMPP/xamppfiles/htdocs/hosts/files"
filesList = []

# CHECK FOR REQUEST
if not os.path.exists( os.path.join(filesDir, "reload.var") ):
	sys.exit()

# READ CURRENT ALLOWED HOSTS
allowedHosts = {}
lines = []
if os.path.exists(hostsAllowFile):
	try:
		file = open(hostsAllowFile, 'r')
		lines = file.readlines()
		file.close()
	except:
		print "Error reading allowed hosts"
if len(lines) > 0:
	for line in lines:
		line = line.strip()
		if not line.startswith('#') and len(line):
			lineService, lineHost = getHost(line)
			if not lineHost in allowedHosts:
				allowedHosts[lineHost] = [lineService]
			else:
				if not lineService in allowedHosts[lineHost]:
					allowedHosts[lineHost] = allowedHosts[lineHost] + [lineService]

# READ HOSTS TO ADD
filesList = []
if os.path.exists(filesDir) and os.path.isdir(filesDir):
	filesList = os.listdir(filesDir)
if len(filesList) > 0:
	hostsToAdd = {}
	for fileName in filesList:
		lines = []
		if fileName.endswith('.host'):
			filePath = os.path.join(filesDir, fileName)
			try:
				file = open(filePath, "r")
				lines = file.readlines()
				file.close()
			except:
				print "Error opening file"
		if len(lines):
			for line in lines:
				line = line.strip()
				if not line.startswith('#') and len(line):
					lineService, lineHost = getHost(line)
					if not lineHost in hostsToAdd:
						hostsToAdd[lineHost] = [lineService]
					else:
						if not lineService in hostsToAdd[lineHost]:
							hostsToAdd[lineHost] = hostsToAdd[lineHost] + [lineService]

# PROCESS HOSTS TO ADD
for host in hostsToAdd:
	if not host in allowedHosts:
		for service in hostsToAdd[host]:
			print service + ':' + host
			os.system("echo '%s: %s' >> %s" % (service, host, hostsAllowFile))
	else:
		for service in hostsToAdd[host]:
			if not service in allowedHosts[host]:
				print service + ':' + host
				os.system("echo '%s: %s' >> %s" % (service, host, hostsAllowFile))

if os.path.exists( os.path.join(filesDir, "reload.var") ):
	os.unlink( os.path.join(filesDir, "reload.var") )
