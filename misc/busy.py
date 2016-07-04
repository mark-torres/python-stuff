#!/usr/bin/env python3
import pyautogui, time, logging, random, os

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
	# pyautogui.press('esc')
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
	moveX = random.randint(-200, 200)
	moveY = random.randint(-200, 200)
	pyautogui.moveRel(moveX, moveY, duration=0.4)
	pyautogui.press('esc')
	return True

# options
actions = [
	'nudgeMouse',
#	'switchApp',
	'scroll',
#	'moveMouse'
]

# START - - - - - - - - -
try:
	print("Press CTRL + C to end program")
	# start loop
	while True:
		action = random.choice(actions)
		if action == 'nudgeMouse':
			nudgeMouse()
		elif action == 'switchApp':
			switchApp()
		elif action == 'scroll':
			scroll()
		elif action == 'moveMouse':
			moveMouse()
		seconds = random.randint(60 * 3, 60 * 6)
		logging.debug("Wait %d mins" % (seconds//60))
		time.sleep(seconds)
except:
	print("\nDone")
