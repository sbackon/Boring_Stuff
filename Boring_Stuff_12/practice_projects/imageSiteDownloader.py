#!/usr/bin/env python3
# imageSiteDownloader.py - goes to imgur.com, searches for the specified term in the command line and downloads the corresponding images

import os, sys, time, requests
from selenium import webdriver

# Save searchterm
search_term = ' '.join(sys.argv[1:])

# Go to imgur
browser = webdriver.Firefox()
browser.get('https://imgur.com/')

# Serach for user given term
searchElem = browser.find_element_by_class_name('Searchbar-textInput')
searchElem.send_keys(search_term)
searchElem.submit()

# Download all corresponding images
time.sleep(2)
imageElems = browser.find_elements_by_css_selector('a img')

if not os.path.exists('Imgur'):
    os.mkdir('Imgur')

os.mkdir('Imgur/' + '_'.join(sys.argv[1:]))

for image in imageElems:
    url_name =  image.get_attribute('src')
    res = requests.get(url_name)
    res.raise_for_status()

    imageFile = open(os.path.join('Imgur/' + '_'.join(sys.argv[1:]), os.path.basename(url_name)), 'wb')
    for chunk in res.iter_content(100000):
        imageFile.write(chunk)
    imageFile.close()
