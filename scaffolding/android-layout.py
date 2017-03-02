#!/usr/bin/env python3

import argparse, os, sys, re
from xml.dom import minidom

# ====================
# = ARGUMENTS PARSER =
# ====================

# https://developer.yahoo.com/python/python-xml.html

parser = argparse.ArgumentParser(description='Parses an XML layout file and generates declaration code for UI elements.')

parser.add_argument('--file','-f',
	dest='layoutFile',
	required=True,
	nargs=1,
	help="Layout XML file to be parsed.")

args = parser.parse_args()

layoutFile = args.layoutFile[0]

# =============
# = FUNCTIONS =
# =============

def id_to_var(idStr, cutter):
	varStr = ""
	parts = idStr.split(cutter)
	if len(parts) == 1:
		return idStr
	else:
		varStr = parts[0]
		for part in parts[1:]:
			varStr += part.title()
		return varStr

def find_elements(domNode):
	"""Recursively look for elements with ID"""
	if not domNode.nodeType == 1:
		return
	# check node
	if domNode.hasAttributes():
		elemClass = domNode.tagName
		elemId = domNode.getAttribute('android:id')
		idRe = re.compile(r'^@\+id\/(\w\w+)$')
		matches = idRe.search(elemId)
		if matches != None:
			elemId = matches.group(1)
			elemVar = id_to_var(elemId, "_")
			print("%s %s = (%s) findViewById(R.id.%s);" % (elemClass, elemVar, elemClass, elemId))
	# check child nodes
	if domNode.hasChildNodes():
		for childNode in domNode.childNodes:
			find_elements(childNode)

# ===========
# = PROGRAM =
# ===========

if not os.path.exists(layoutFile):
	print("The file does not exist")
	sys.exit()

if not os.access(layoutFile, os.R_OK):
	print("The file is not readable")
	sys.exit()

layoutDom = minidom.parse(layoutFile)

if not layoutDom.hasChildNodes():
	print("The document is empty")
	sys.exit()

topElement = layoutDom.childNodes[0]
find_elements(topElement)
# EOF
