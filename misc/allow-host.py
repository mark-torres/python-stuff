#!/usr/bin/env python
import sys, re, os

# Services List: /etc/services

hosts_file = "/etc/hosts.allow"
re_ip = re.compile(r"^\d+\.\d+(\.(\d+|\*)){2}$")
re_allow_line = re.compile(r"^\w+:")

services = {
	'sshd' : "SSH",
	'ftpd' : "FTP",
	'http' : "Web",
	'https': "Secure Web",
}

if len(sys.argv[1:]) > 0:
	ip = sys.argv[1]
else:
	print "No IP provided. Nothing to do"
	print ""
	print "Add host IP to allowed hosts"
	print "Usage: "
	print sys.argv[0] + " HOST_IP [sshd|ftpd|http|https]"
	exit()
	
if len(sys.argv[2:]) > 0:
	service = sys.argv[2]
else:
	service = "sshd"

if service not in services:
	service = "sshd"

# ===============
# = VALIDATIONS =
# ===============
if not os.path.exists(hosts_file):
	print "Could not read file: '%s'" % hosts_file

if not re_ip.match(ip):
	print "Invalid IP provided: " + ip
	exit()

print "Adding '%s' to allowed hosts file..." % ip

found = False

hosts_allow = open(hosts_file)

try:
	for line in hosts_allow:
		if re_allow_line.match(line):
			if line.find(service) >= 0 and line.find(ip) >= 0:
				found = True
except Exception, e:
	print "Error reading file"
finally:
	hosts_allow.close()

if not found:
	os.system("echo '%s: %s' >> %s" % (service, ip, hosts_file))
	print "Done!"
else:
	print "IP already allowed for " + services[ service ]
