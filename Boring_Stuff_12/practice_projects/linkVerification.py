#!/usr/bin/env python3
# linkVerification.py - given the URL of a web page, will attempt to download every linked page on the page. The program should flag any pages that have a 404 “Not Found” status code and print them out as broken links.

import requests, sys, bs4, os, re

res = requests.get(sys.argv[1])
res.raise_for_status()
webSoup = bs4.BeautifulSoup(res.text, 'html.parser')

if not os.path.exists('Linked_Sites'):
    os.mkdir('Linked_Sites')

urlRegex = re.compile(r'https://')
counter = 1
for link in webSoup.find_all('a'):
    if link.get('href') != None:
        if urlRegex.search(link.get('href')) != None:
            tempRes = requests.get(link.get('href'))

            if tempRes.status_code == 404:
                print('Not Found: ' + link.get('href'))

            else:
                tempFile = open(os.path.join('Linked_Sites', str(counter)), 'wb')
                counter += 1
                for chunk in tempRes.iter_content(100000):
                    tempFile.write(chunk)
                tempFile.close()
