#!/usr/bin/env python3
import argparse, requests, logging, sys, os, json

# =====================
# = SET LOGGING LEVEL =
# =====================

logging.basicConfig(level=logging.ERROR, format= '%(asctime)s - %(levelname)s - %(message)s')

# ====================
# = ARGUMENTS PARSER =
# ====================

parser = argparse.ArgumentParser(description='Gets the accounts list feed for UrVenue and UrRides apps.')

parser.add_argument('--sessionkey','-k',
	dest='sessionkey',
	required=True,
	nargs=1,
	help="A valid session key.")
	
parser.add_argument('--app','-a',
	dest='app',
	choices=['urvenue','urrides'],
	required=True,
	nargs=1,
	help="Mobile application.")
	
args = parser.parse_args()

sessionKey = ""
appName = ""

try:
	sessionKey = args.sessionkey[0]
	appName = args.app[0]
except Exception as e:
	logging.error("Error getting parameters.")
	sys.exit()

logging.info( "Using KEY = '%s' APP = '%s'" % (sessionKey, appName) )

apiEndpoints = {
	"urvenue": "https://api.urvenue.me/v1/uvapp/routing/json/get",
	"urrides": "https://api.urvenue.me/v1/uvapp/riderouting/json/get",
}

apiEndpoint = apiEndpoints[appName]
tmpFilename = "accounts.tmp"
getData = {
	"apikey": sessionKey,
	"sourcecode": "users",
	"sourceloc": "uvdev",
}

# make request
responseText = ""

try:
	logging.info("Requesting accounts list...")
	req = requests.get(apiEndpoint, getData)
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

# show accounts list
if "uv" in response and "data" in response["uv"] and isinstance(response["uv"]["data"], list):
	print("Accounts found:")
	for account in response["uv"]["data"]:
		print("+ %s" % (account["targetname"]))
		print("  - Target URL [%s]" % (account["targeturl"]))
		print("  - Target logout URL [%s]" % (account["targetlogout"]))
else:
	print("No accounts found")
