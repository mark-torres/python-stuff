#!/usr/bin/env python3
from selenium import webdriver

browser = webdriver.Firefox()

# load login page
browser.get('https://login.yahoo.com/')

# fill username and password fields
emailElem = browser.find_element_by_id('login-username')
passwordElem = browser.find_element_by_id('login-passwd')
emailElem.send_keys('my_username')
passwordElem.send_keys('12345')

# submit form
passwordElem.submit()

# go to email page
browser.get('https://mail.yahoo.com')

# get compose button
btnCompose = browser.find_element_by_css_selector('#Compose > button')
btnCompose.click()

# fill all fields
toField = browser.find_element_by_id('to-field')
subjectField = browser.find_element_by_id('subject-field')
rteText = browser.find_element_by_id('rtetext')

toField.send_keys('markitos.mets@gmail.com')
subjectField.send_keys('Testing Selenium webdriver')
rteText.send_keys('Sent using Selenium webdriver from Python :)')

# get send button
sendButton = browser.find_element_by_link_text('Enviar')
sendButton.click()

# sign out
btnSignOut = browser.find_element_by_id('yucs-signout')
btnSignOut.click()

# close browser
browser.quit()
