#!/usr/bin/env python3
import time, random
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

browser = webdriver.Firefox()

browser.get('https://gabrielecirulli.github.io/2048/')
htmlElem = browser.find_element_by_tag_name('html')

gameOver = False
btnRetry = browser.find_element_by_class_name('retry-button')
keys = [Keys.DOWN, Keys.UP, Keys.LEFT, Keys.RIGHT]

while not gameOver:
	# check if game over
	gameOver = btnRetry.is_displayed()
	# send random key
	key = keys[ random.randint(0, len(keys) - 1) ]
	htmlElem.send_keys(key)
	# pause 0.5 secs before next move
	time.sleep(0.5)

print('DONE!')
