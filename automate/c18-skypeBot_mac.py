#!/usr/bin/env python3
import pyautogui, time, logging, random, sys

skypeNames = [
	"gabriele.barriosd",
	"momp",
	"eziranda"
]

# NOTE: the typewrite() function is affected by the keyboard configuration
# If you want to avoid problems, just use the US english layout for your keyboard
messages = [
	"jajaja https://www.youtube.com/watch?v=Z1XJgQjcowM",
	"ya viste esta serie? https://www.youtube.com/watch?v=1UaA5UkoZKw",
	"un taco de ojo https://www.youtube.com/watch?v=-d5FtGhaQAc",
	"el reto del condon https://www.youtube.com/watch?v=aDMd6BeReAI",
	"jajaja https://www.youtube.com/watch?v=qvpd6A5NMyc",
	"random video https://www.youtube.com/watch?v=NI95LMyPGcc",
	"mas random https://www.youtube.com/watch?v=vyIBxbLimlc",
	"otro video https://www.youtube.com/watch?v=76W37_vZ6Xg"
]

skypeIconRegion = pyautogui.locateOnScreen('../tmp/app-skype.png')
skypeSearchRegion = None
if skypeIconRegion != None:
	for contact in skypeNames:
		# click skype icon
		pyautogui.click( pyautogui.center(skypeIconRegion) )
		if skypeSearchRegion == None:
			skypeSearchRegion = pyautogui.locateOnScreen('../tmp/skype-numpad.png')
		if skypeSearchRegion != None:
			# find contact
			skypeNumpadX, skypeNumpadY = pyautogui.center(skypeSearchRegion)
			skypeSearchPos = (skypeNumpadX + 150, skypeNumpadY)
			pyautogui.click(skypeSearchPos)
			pyautogui.typewrite( contact )
			time.sleep(2)
			pyautogui.press('enter')
			# send message
			pyautogui.typewrite( random.choice(messages) )
			pyautogui.press('enter')
