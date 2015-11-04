#! /usr/local/bin/python3
import re

def re_strip(text, replace = None):
	"""REGEX version of strip"""
	if replace == None:
		replace = '\s'
	else:
		toks = list(replace)
		replace = '('+'|'.join(toks)+')'
	regex = r'^'+replace+'+|'+replace+'+$'
	reStrip = re.compile(regex)
	return reStrip.sub('',text);

text = ' skl    \n\n'
print(text)
print(re_strip(text))

text = 'eeeeso es todoooo'
print(text)
print(re_strip(text, 'aeiou'))

