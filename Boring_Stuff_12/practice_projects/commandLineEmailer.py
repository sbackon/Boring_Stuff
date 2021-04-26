#!/usr/bin/env python3
# commandLineEmailer.py takes email adress and string and sends them from your mail

import sys, time
from selenium import webdriver
from selenium.webdriver.support.ui import Select

# Save given email and string
target_email = sys.argv[1]
etext = sys.argv[2:]

# Open webbrowser and log in to your account
browser = webdriver.Firefox()
browser.get('https://www.trash-mail.com/posteingang/')

# ???? added instead of real one to not reveal actual account name and login
endingElem = Select(browser.find_element_by_id('form-domain-id'))
endingElem.select_by_visible_text('?????')

enameElem = browser.find_element_by_id('inputEmail')
enameElem.send_keys('????')
enameElem.submit()

# Select write email option
time.sleep(2)
writeElem = browser.find_element_by_partial_link_text('Schreiben')
writeElem.click()
time.sleep(2)

# Enter provided email address and text
recipient = browser.find_element_by_id('form-to')
recipient.send_keys(target_email)

textField = browser.find_element_by_id('editor')
textField.send_keys(etext)

# Press send button
subButton = browser.find_element_by_id('send-mails')
subButton.click()
