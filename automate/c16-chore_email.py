#!/usr/bin/env python3
import smtplib, sys, shelve, os, random, getpass
# Import the email modules we'll need
from email.mime.text import MIMEText

chores = [
	'laundry',
	'ironing',
	'beds',
	'dishes',
	'bathroom',
	'vacuum'
]

emails = [
	'some@hotmail.com',
	'some@gmail.com',
	'some@yahoo.com'
]

if len(chores) < len(emails):
	print("Number of chores is less than the number of people")
	sys.exit()

# load assignments
saveFile = os.path.join("..","tmp","chore_email.sav")
try:
	settingsShelf = shelve.open(saveFile, flag = 'c', writeback = True)
except:
	print("Error creating/loading settings file")
	sys.exit()

if 'assignments' in settingsShelf:
	assignments = settingsShelf['assignments']
else:
	assignments = {}

# populate assignments dictionary if needed
for i in range(0, len(emails)):
	if not emails[i] in assignments:
		assignments[ emails[i] ] = {
			'last': None
		}

# assign chores
assignedChores = []
for i in range(0, len(emails)):
	done = False
	while not done:
		newChore = random.choice(chores)
		if newChore not in assignedChores and newChore != assignments[ emails[i] ]['last']:
			done = True
			assignedChores.append(newChore)
			assignments[ emails[i] ]['last'] = newChore

# email assignments
emailSent = False
smtpServer = "smtp.mail.yahoo.com"
smtpPort = 587
smtpUser = "some@yahoo.com"
smtpPass = ""

while len(smtpPass) == 0:
	smtpPass = getpass.getpass("Enter password for email '%s'" % smtpUser)
	smtpPass.strip()

print("Attempting to connect to SMTP server",smtpServer,"...")

yahoo = smtplib.SMTP(smtpServer, smtpPort)
yahoo.ehlo()
yahoo.starttls()
yahoo.login(smtpUser, smtpPass)

for email in assignments:
	print("Emailing " + email)
	msg = MIMEText('Your chore this week is: '+ assignments[email]['last'])
	msg['Subject'] = "Weekly chore assignment"
	msg['From'] = "Mark Torres <%s>" % smtpUser
	msg['To'] = email
	yahoo.send_message(msg)

yahoo.quit()
# save assignments if email was sent
settingsShelf['assignments'] = assignments
settingsShelf.sync()
settingsShelf.close()
