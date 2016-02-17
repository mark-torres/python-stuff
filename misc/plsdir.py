#!/usr/bin/env python
import sys

if len(sys.argv) > 1:
	print("[playlist]")
	print("NumberOfEntries=%d" % len(sys.argv[1:]))
	for i in range(1, len(sys.argv)):
		print("File%d=%s" % (i, sys.argv[i]))
