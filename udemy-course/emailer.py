import imaplib, smtplib, os
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText

# SETTINGS VARS
sender_addr = 'NOT SET'
sender_user = ''
sender_pass = ''

# CONFIGURE
def configure(ref = ''):
	os.system("clear")
	global sender_addr, sender_user, sender_pass
	sender_addr = raw_input("Enter your GMail address: ")
	sender_user = sender_addr
	sender_pass = raw_input("Enter your password: ")
	if ref == 'read':
		read()
	elif ref == 'send':
		send()
	else:
		menu()

# READ
def read():
	global sender_user, sender_pass
	if len(sender_user) == 0:
		configure('read')
	else:
		os.system("clear")
		mailserver = imaplib.IMAP4_SSL('imap.gmail.com', 993)
		mailserver.login(sender_user, sender_pass)
		status, count = mailserver.select('Inbox')
		status, data = mailserver.fetch(count[0], '(UID BODY[TEXT])')
		print data[0][1]
		mailserver.close()
		mailserver.logout()
		choice = raw_input("Press ENTER to return to menu")
		menu()

# SEND
def send():
	global sender_addr, sender_user, sender_pass
	if len(sender_user) == 0:
		configure('send')
	else:
		os.system("clear")
		dest_addr = raw_input("Enter destination email: ")
		subject = raw_input("Enter the subject: ")
		text = raw_input("Enter message to send: ")
		
		print("\nSending mail, please wait...\n")
	
		msg   = MIMEMultipart()
		msg['From']    = sender_addr
		msg['To']      = dest_addr
		msg['Subject'] = subject

		msg.attach(MIMEText(text))
		server = smtplib.SMTP("smtp.gmail.com:587")
		server.ehlo()
		server.starttls()
		server.ehlo()
		server.login(sender_user, sender_pass)
		server.sendmail(sender_addr, dest_addr, msg.as_string())
		server.quit()
		choice = raw_input("Email sent. Press ENTER to return to menu")
		menu()

# MENU
def menu():
	global sender_addr
	os.system("clear")
	print("GMail user: %s" % sender_addr)
	print("")
	print("1) Read email")
	print("2) Send email")
	print("3) Configure email")
	print("4) Exit")
	print("")
	choice = raw_input("Enter a choice: ")
	if choice == '1':
		read()
	elif choice == '2':
		send()
	elif choice == '3':
		configure()
	elif choice == '4':
		os.system("clear")
		exit()
	else:
		menu()

# ===============
# = RUN PROGRAM =
# ===============
while 1:
	menu()
