#!/usr/bin/env python3
import pyautogui, time, logging, random, sys

# fail-safe
pyautogui.PAUSE = 0.3
pyautogui.FAILSAFE = True
# logging
logging.basicConfig(level=logging.DEBUG, format='%(levelname)s - %(message)s')
logging.disable(logging.CRITICAL)

# functions
def nudgeMouse():
	logging.debug("nudgeMouse")
	moveX = random.randint(-50, 50)
	moveY = random.randint(-50, 50)
	pyautogui.moveRel(moveX, moveY, duration=0.1)
	moveX = random.randint(-50, 50)
	moveY = random.randint(-50, 50)
	pyautogui.moveRel(moveX, moveY, duration=0.1)
	moveX = random.randint(-50, 50)
	moveY = random.randint(-50, 50)
	pyautogui.moveRel(moveX, moveY, duration=0.1)
	pyautogui.press('esc')
	return True

def switchApp():
	logging.debug("switchApp")
	tabs = random.randint(1, 20)
	pyautogui.keyDown('command')
	for i in range(0, tabs):
		pyautogui.press('tab')
	pyautogui.keyUp('command')
	scroll()
	return True

def scroll():
	logging.debug("scroll")
	pyautogui.scroll(random.randint(-100, 100))
	return True

def moveMouse():
	logging.debug("moveMouse")
	moveX = random.randint(-300, 300)
	moveY = random.randint(-300, 300)
	pyautogui.moveRel(moveX, moveY, duration=0.2)
	pyautogui.press('esc')
	return True

def clickApp(appName, appIconPos):
	logging.debug("Click on app: %s" % appName)
	pyautogui.click( pyautogui.center(appIconPos) )
	moveMouse()
	scroll()
	return True

# options
actions = [
	'nudgeMouse',
	'switchApp',
	'clickApp',
	'scroll',
	'moveMouse'
]

apps = {
	"atom": {
		"icon": "../tmp/app-atom.png",
		"pos": None
	},
	"ffox": {
		"icon": "../tmp/app-ffox.png",
		"pos": None
	},
	"ffox_dev": {
		"icon": "../tmp/app-ffox_dev.png",
		"pos": None
	},
	"skype": {
		"icon": "../tmp/app-skype.png",
		"pos": None
	},
	"source_tree": {
		"icon": "../tmp/app-source_tree.png",
		"pos": None
	},
	"spotify": {
		"icon": "../tmp/app-spotify.png",
		"pos": None
	},
	"terminal": {
		"icon": "../tmp/app-terminal.png",
		"pos": None
	},
	"text_wrangler": {
		"icon": "../tmp/app-text_wrangler.png",
		"pos": None
	},
	"textmate": {
		"icon": "../tmp/app-textmate.png",
		"pos": None
	},
	"upwork": {
		"icon": "../tmp/app-upwork.png",
		"pos": None
	}
}

appNames = list(apps.keys())
# find app icons on screen and save position
print("Looking for apps..")
for appName in apps:
	try:
		iconPos = pyautogui.locateOnScreen(apps[appName]['icon'])
		if iconPos != None:
			apps[appName]['pos'] = iconPos
	except Exception as e:
		logging.debug("Error locating %s icon" % appName)

try:
	print("Press CTRL + C to end program")
	# start loop
	while True:
		action = random.choice(actions)
		if action == 'nudgeMouse':
			nudgeMouse()
		elif action == 'switchApp':
			switchApp()
		elif action == 'clickApp':
			appName = random.choice(appNames)
			if apps[appName]['pos'] != None:
				clickApp(appName, apps[appName]['pos'])
			else:
				continue
		elif action == 'scroll':
			scroll()
		elif action == 'moveMouse':
			moveMouse()
		seconds = random.randint(4, 6)
		logging.debug("Wait %d secs" % seconds)
		time.sleep(seconds)
except:
	print("\nDone")
