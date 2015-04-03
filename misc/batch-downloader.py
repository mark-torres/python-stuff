#!/usr/bin/env python
import sys, re
from os import system as console
# GLOBAL VARIABLES
out_dir = "downloads"
# regular expressions
re_int = '^\d+$'
re_folder = '^\w+$'
re_pattern = '(^.+)(\[(\d+)\-(\d+)\])(.+$)'
# = = = = = = = = = = = = = = = = = = = = = =
def process_pattern(pattern):
	links = []
	if re.match(re_pattern, pattern):
		matches = re.search(re_pattern, pattern)
		left_side = matches.group(1)
		right_side = matches.group(5)
		limit_a = int(matches.group(3))
		limit_b = int(matches.group(4))
		step = 1
		if limit_a > limit_b:
			tmp, limit_a = limit_b, limit_a
			limit_b = tmp
		while limit_a < limit_b:
			links.append(left_side+str(limit_a)+right_side)
			# print("%s%s%s" % (left_side, limit_a, right_side))
			limit_a += step
	return links
# = = = = = = = = = = = = = = = = = = = = = =

# get parameters
pattern = ''
download = False
mode = "print"
if len(sys.argv[1:]) > 0:
	pattern = sys.argv[1]
else:
	print("No pattern supplied. Nothing to do.")
	exit()

if len(sys.argv[2:]) > 0:
	download = True

if len(sys.argv[3:]) > 0:
	mode = sys.argv[3]

if mode == 'gallery':
	download = False

processed_list = process_pattern(pattern)

if len(processed_list) > 0:
	if download:
		for item in processed_list:
			console("wget --no-clobber --wait=2 "+item)
	elif mode == 'gallery':
		print("<html><head><title>"+pattern+"</title></head><body>")
		for item in processed_list:
			print('<div style="background-image: url(\'%s\');background-size: contain;background-repeat: no-repeat;background-position: center;width: 300px; height: 300px; float: left; border: 1px solid silver;"><img style="display: none;" alt="%s" src="%s"/></div>' % (item, item, item))
		print("</body></html>")
	else:
		for item in processed_list:
			print(item)
else:
	print("Invalid pattern: %s" % pattern)
