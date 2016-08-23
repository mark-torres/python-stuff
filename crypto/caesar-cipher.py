#!/usr/bin/env python3
import argparse, sys

parser = argparse.ArgumentParser(description="Encrypts a message using Caesar cipher.")

parser.add_argument("--key","-k",
	dest="key",
	required=True,
	nargs=1,
	type=int,
	help="Cipher key.")

parser.add_argument("--plain","-p",
	dest="plainMessage",
	nargs=1,
	help="A single-quoted message to be encrypted.")

parser.add_argument("--encrypted","-e",
	dest="secretMessage",
	nargs=1,
	help="A single-quoted encrypted message to be decrypted.")

args = parser.parse_args()

cipherKey = args.key[0]
plainMessage = args.plainMessage[0].upper() if (args.plainMessage != None) else None
secretMessage = args.secretMessage[0].upper() if (args.secretMessage != None) else None

alphabet = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
alphaSize = len(alphabet)

# =============
# = Functions =
# =============
def caesar_encrypt(key, message):
	encrypted = []
	for i in range( len(message) ):
		if (message[i] in alphabet):
			pos = alphabet.index( message[i] )
			pos = pos + key
			if (pos not in range( alphaSize )):
				pos = pos - alphaSize
			encrypted.append(alphabet[pos])
		else:
			encrypted.append(message[i])
	return ''.join(encrypted)

def caesar_decrypt(key, message):
	decrypted = []
	for i in range( len(message) ):
		if (message[i] in alphabet):
			pos = alphabet.index( message[i] )
			pos = pos - key
			if (pos not in range( alphaSize )):
				pos = pos + alphaSize
			decrypted.append(alphabet[pos])
		else:
			decrypted.append(message[i])
	return ''.join(decrypted)

# ==================
# = Implementation =
# ==================

# validate key value
if cipherKey not in range( 1, alphaSize ):
	print("The key must be a number between 1 and %s" % ( alphaSize - 1 ))
	sys.exit()

# validate message
if (plainMessage == None and secretMessage == None):
	print("You need to provide a message to encrypt/decrypt.")
	sys.exit()
elif (plainMessage != None and secretMessage != None):
	print("You should only provide either a plain or an encrypted message, not both.")
	sys.exit()

if (plainMessage != None):
	# print("Plain message: %s" % (plainMessage))
	print("Encrypted message: %s" % (caesar_encrypt(cipherKey, plainMessage)))
elif (secretMessage != None):
	# print("Encrypted message: %s" % (secretMessage))
	print("Plain message: %s" % (caesar_decrypt(cipherKey, secretMessage)))


