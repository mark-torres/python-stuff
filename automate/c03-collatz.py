#! /usr/local/bin/python3

# read number
def readint(message):
	"""Reads a number from the console"""
	if len(message) == 0:
		message = "Enter an integer number:"
	while True:
		try:
			num = int(input(message+" "))
			break
		except:
			print ("Please enter a valid integer number")
	return num

# collatz
def collatz(number):
	"""collatz sequence"""
	result = 0
	if number % 2 == 0:
		result = number // 2
	if number % 2 == 1:
		result = 3 * number + 1
	print( str(result) )
	return result

usernumber = readint("Enter a number (1 to quit):")
while usernumber != 1:
	usernumber = collatz(usernumber)