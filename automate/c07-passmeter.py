#! /usr/local/bin/python3
import re

def passwordMeter(password):
	"""docstring for passwordMeter"""
	secureAspects = {}
	secureAspects.setdefault('length', False)
	secureAspects.setdefault('lowercase', False)
	secureAspects.setdefault('uppercase', False)
	secureAspects.setdefault('digit', False)
	score = 0
	maxScore = len(secureAspects)
	# check length
	if len(password) >= 8:
		secureAspects['length'] = True;
	# check lowercase
	reLower = re.compile(r'[a-z]')
	if reLower.search(password) != None:
		secureAspects['lowercase'] = True
	# check uppercase
	reUpper = re.compile(r'[A-Z]')
	if reUpper.search(password) != None:
		secureAspects['uppercase'] = True
	# check digit
	reDigit = re.compile(r'[0-9]')
	if reDigit.search(password) != None:
		secureAspects['digit'] = True
	# get score
	for aspect in secureAspects:
		if secureAspects[aspect]:
			score += 1
	return int( score / maxScore * 100 )

password = 'Hola'
score = passwordMeter(password)
print('Score for', password, ':', score)

password = 'Yes, sir, 700'
score = passwordMeter(password)
print('Score for', password, ':', score)

password = 'Regex Objects'
score = passwordMeter(password)
print('Score for', password, ':', score)

password = 'u7958Xn2YfH684A74782jX5A'
score = passwordMeter(password)
print('Score for', password, ':', score)


