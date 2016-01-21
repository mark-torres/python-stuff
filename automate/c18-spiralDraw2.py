#!/usr/bin/env python3
import pyautogui, time
time.sleep(5)
# select poliline tool
# click to put drawing program in focus
pyautogui.click()
distance = 200
while distance > 0:
	pyautogui.moveRel(distance, 0, duration=0.2)   # move right
	pyautogui.click()
	distance = distance - 5
	pyautogui.moveRel(0, distance, duration=0.2)   # move down
	pyautogui.click()
	pyautogui.moveRel(-distance, 0, duration=0.2)  # move left
	pyautogui.click()
	distance = distance - 5
	pyautogui.moveRel(0, -distance, duration=0.2)  # move up
	pyautogui.click()
