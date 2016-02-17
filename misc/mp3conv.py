#!/usr/bin/env python
import sys, os

bitRate = 160

if len(sys.argv) > 1:
	files = sys.argv[1:]
	for filename in files:
		filename = filename.replace("'", "\\'")
		name, ext = os.path.splitext(filename)
		convFile = "%s@%dk%s" % (name, bitRate, ext)
		print("ffmpeg -i '%s' -codec:a libmp3lame -b:a %dk '%s'" % (filename, bitRate, convFile))
