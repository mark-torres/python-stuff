#!/usr/bin/env python3
import argparse, requests, logging, sys, os, json

# =====================
# = SET LOGGING LEVEL =
# =====================

logging.basicConfig(level=logging.ERROR, format= '%(asctime)s - %(levelname)s - %(message)s')

# ====================
# = ARGUMENTS PARSER =
# ====================

parser = argparse.ArgumentParser(description='Gets a UVME session key using UVME API.')

parser.add_argument('--loginkey','-k',
	dest='loginkey',
	required=True,
	nargs=1,
	help="A valid login key.")
	
args = parser.parse_args()

loginKey = ""

try:
	loginKey = args.loginkey[0]
except Exception as e:
	logging.error("Error getting parameters.")
	sys.exit()

logging.info( "Using KEY = '%s'" % (loginKey) )


sessionKeyEndpoint = "https://api.urvenue.me/v1/users/loginkey/json/get"
tmpFilename = "session_key.tmp"
getData = {
	"apikey": loginKey,
	"sourcecode": "users",
	"sourceloc": "uvdev",
}

# make request
responseText = ""

try:
	logging.info("Requesting login key...")
	req = requests.get(sessionKeyEndpoint, getData)
	responseText = str(req.text)
	# save response text
	cwd = os.getcwd()
	if os.access(cwd,os.W_OK):
		logging.info("Saving response to '%s'..." % (tmpFilename) )
		filename = os.path.join(cwd, tmpFilename)
		fh = open(filename, "w")
		fh.write(responseText + "\n")
		fh.close()
	else:
		logging.debug(responseText)
except Exception as e:
	logging.error( str(e) )
	sys.exit()

# decode response
response = {}

try:
	response = json.loads(responseText)
except Exception as e:
	logging.error( str(e) )
	sys.exit()

# show session key
if "uv" in response and "data" in response["uv"] and "sessionkey" in response["uv"]["data"]:
	print("Session key:", response["uv"]["data"]["sessionkey"])
else:
	print("Session key not found in response")

# show topics data
if "uv" in response and "data" in response["uv"] and "sc8" in response["uv"]["data"] and "channels" in response["uv"]["data"]["sc8"]:
	print("Topics found:")
	for topic, title in response["uv"]["data"]["sc8"]["channels"].items():
		print("- %s [%s]" % (title, topic))