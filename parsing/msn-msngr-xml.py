#!/usr/bin/env python3

# https://www.tutorialkart.com/python/python-xml-parsing/

import xml.etree.ElementTree as ET
import sys, argparse, os

parser = argparse.ArgumentParser(description='Parses a MSN conversation log in XML format.')

parser.add_argument('--file','-f',
	dest='logFile',
	required=True,
	nargs=1,
	help="Log file to be parsed.")

args = parser.parse_args()

logFile = args.logFile[0]


#====================
def msn_parse_message(msg_xml):
	msg_data = {}
	msg_data['date'] = msg_xml.attrib['Date']
	msg_data['time'] = msg_xml.attrib['Time']
	msg_data['session'] = msg_xml.attrib['SessionID']
	msg_data['user'] = ""
	msg_data['text'] = ""
	for child in msg_xml:
		if child.tag == "From":
			msg_data['user'] = child[0].attrib['FriendlyName']
		if child.tag == "Text":
			msg_data['text'] = child.text
	return msg_data

def msn_message_text(message):
	print("- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -")
	print("[%s@%s] %s:"
		%
		(message['date'], message['time'], message['user'])
	)
	print(message['text'])
#====================
if not os.path.exists(logFile):
	print("The file does not exist")
	sys.exit()

if not os.access(logFile, os.R_OK):
	print("The file is not readable")
	sys.exit()

tree = ET.parse(logFile)
root = tree.getroot()

# check tree root
if root.tag != "Log":
	print("Log root not found. Nothing to do here.")
	sys.exit(0)

# Set session ID
sess_id = "0"
# Loop all messages
for msg in root:
	if msg.tag == "Message":
		msg_data = msn_parse_message(msg)
		# check session id
		msg_sess = msg_data['session']
		if msg_sess != sess_id:
			print("================================= SessionID %s" % (msg_sess))
			sess_id = msg_sess
		msn_message_text(msg_data)

