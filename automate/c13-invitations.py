#!/usr/bin/env python3
import argparse, sys, docx, os, random

parser = argparse.ArgumentParser(description='Create custom invitations as Word documents')

parser.add_argument('--template','-t',
	dest='templateDoc',
	required=True,
	nargs=1,
	help="Word document to use as template")
parser.add_argument('--data','-d',
	dest='dataFile',
	required=True,
	nargs=1,
	help="Text file with names, one per line.")
args = parser.parse_args()

# REQUIRED ARGS
templateDocPath = args.templateDoc[0]
dataFilePath = args.dataFile[0]

# VALIDATE
if not os.path.isfile(templateDocPath):
	print("Template file does not exist")
	sys.exit()
if not os.path.isfile(dataFilePath):
	print("Data file does not exist")
	sys.exit()

outFileName = "invitations%d.docx" % (random.randint(100, 999))
outFileDir = os.path.dirname(templateDocPath)
outFilePath = os.path.join(outFileDir, outFileName)

try:
	# use template
	tplDoc = docx.Document(templateDocPath)
except Exception as e:
	print("Error reading template document")

# delete paragraphs if any
# https://github.com/python-openxml/python-docx/issues/33#issuecomment-77661907
for paragraph in tplDoc.paragraphs:
	p = paragraph._element
	p.getparent().remove(p)
	p._p = p._element = None

dataFile = open(dataFilePath, "r")
names = dataFile.readlines()

if len(names) == 0:
	print("Data file is empty")
	sys.exit()
else:
	for name in names:
		name = name.strip()
		if len(name) > 0:
			tplDoc.add_paragraph("It would be a pleasure to have the company of", style = 'Invitation text')
			tplDoc.add_paragraph(name, style = 'Invitation title')
			tplDoc.add_paragraph("at 11010 Memory Lane on the Evening of", style = 'Invitation text')
			tplDoc.add_paragraph("April 1st", style = 'Invitation title')
			tplDoc.add_paragraph("at 7 o'clock", style = 'Invitation text')
			# add page break
			tplDoc.add_page_break()

tplDoc.save(outFilePath)
