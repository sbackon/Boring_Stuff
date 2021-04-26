#!/usr/bin/env python3
# reTxt.py - searches all .txt files in the current working directory
#            for a user supplies regualer expression

import sys, re, os
from pathlib import Path

# Make regex from supplied string
sRegex = re.compile(sys.argv[1])
p = Path.cwd()
fileList = list(p.glob('*.txt'))

# Go trhough each file line by line and print matching ones
for item in fileList:
    fileName = os.path.basename(item)
    currentFile = open(fileName, 'r')
    for line in currentFile:
        if sRegex.search(line):
            print(line)
    currentFile.close()


