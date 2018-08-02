#!/usr/bin/env python3
import argparse, requests, logging, sys, os, json
from datetime import datetime

# =====================
# = SET LOGGING LEVEL =
# =====================

logging.basicConfig(level=logging.INFO, format= '%(asctime)s - %(levelname)s - %(message)s')

# ====================
# = ARGUMENTS PARSER =
# ====================

parser = argparse.ArgumentParser(description='Gets a UVME login key using UVME API.')

parser.add_argument('--apikey','-k',
	dest='apikey',
	required=True,
	nargs=1,
	help="A valid global API key.")
	
parser.add_argument('--email','-e',
	dest='email',
	required=True,
	nargs=1,
	help="User's email.")
	
parser.add_argument('--password','-p',
	dest='password',
	required=True,
	nargs=1,
	help="User's password.")
	
args = parser.parse_args()

apiKey = ""
email = ""
password = ""

try:
	apiKey = args.apikey[0]
	email = args.email[0]
	password = args.password[0]
except Exception as e:
	logging.error("Error getting parameters.")
	sys.exit()

logging.info( "Using KEY = '%s' EMAIL = '%s' PASSWD = '%s'" % (apiKey, email, password) )

now = datetime.now()
keyName = "Python " + now.strftime("%Y-%m-%d %H:%M:%S")
loginKeyEndpoint = "https://api.urvenue.me/v1/users/loginkey/json/post"
postData = {
	"apikey": apiKey,
	"sourcecode": "users",
	"sourceloc": "uvdev",
	"email": email,
	"password": password,
	"keyname": keyName,
}

# make request
responseText = ""

try:
	logging.info("Requesting login key...")
	req = requests.post(loginKeyEndpoint, postData)
	responseText = str(req.text)
	# save response text
	cwd = os.getcwd()
	if os.access(cwd,os.W_OK):
		filename = os.path.join(cwd, "login_key.tmp")
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

if "uv" in response:
	if "data" in response["uv"] and "loginkey" in response["uv"]["data"]:
		print("Login key:", response["uv"]["data"]["loginkey"])
	else:
		print("No login key found in response.")
else:
	logging.error("Missing data in response.")
	

