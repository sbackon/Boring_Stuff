#!/usr/bin/env python3
# 2048.py - play the 2048 game by sending up, right, down, left all the time till you loose

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

# Open site
browser = webdriver.Firefox()
browser.get('https://gabrielecirulli.github.io/2048/')

# Spam keys
elem = browser.find_element_by_tag_name('body')
while True:
    elem.send_keys(Keys.UP)
    elem.send_keys(Keys.RIGHT)
    elem.send_keys(Keys.DOWN)
    elem.send_keys(Keys.LEFT)
