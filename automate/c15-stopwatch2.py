#!/usr/bin/env python3

import time, pyperclip

# Display the program's instructions.
print('Press ENTER to begin. Afterwards, press ENTER to "click" the stopwatch. Press Ctrl-C to quit.')
input()                    # press Enter to begin
print('Started.')
startTime = time.time()    # get the first lap's start time
lastTime = startTime
lapNum = 1

lines = []

try:
	while True:
		input()
		lapTime = round(time.time() - lastTime, 2)
		totalTime = round(time.time() - startTime, 2)
		strLapNum = str(lapNum)
		strLapTime = str(lapTime)
		strTotalTime = str(totalTime)
		line = 'Lap #%s %s secs (%s secs)' % (strLapNum.ljust(3), strLapTime.rjust(6), strTotalTime.rjust(7))
		lines.append(line)
		print(line , end = '')
		lapNum += 1
		lastTime = time.time() # reset the last lap time
except KeyboardInterrupt:
	# Handle the Ctrl-C exception to keep its error message from displaying.
	print('\nDone.')

# save to clipboard
pyperclip.copy( "\n".join(lines) )
