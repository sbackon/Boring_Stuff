#!/usr/bin/env python3
# deletingUnneededFiles.py - searches for large files and folders and prints them to the screen

import os
from pathlib import Path

# Set path from where large files are searched downwards, set size above which files should be listed
p = Path('/home/jake/linuxPlayground')
set_size = 800000

for foldername, subfolders, filenames in os.walk(p):

    folderSize = 0

    for filename in filenames:
        realPath = foldername + '/' + filename
        i = os.path.getsize(realPath)
        if i > set_size:
            print(realPath + ' has file size of: ' + str(i))
        folderSize += i

    if folderSize > set_size:
        print(foldername + ' has folder size of: ' + str(folderSize) + '\n')
