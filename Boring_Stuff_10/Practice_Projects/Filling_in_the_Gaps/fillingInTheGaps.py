#!/usr/bin/env python3
# fillingInTheGaps.py - Finds all files with a given prefix, such as spam001.txt, spam002.txt, and so on, in a single folder and locates any gaps in the numbering (such as if there is a spam001.txt and spam003.txt but no spam002.txt). Have the program rename all the later files to close this gap.

import re, shutil, os

# Prefix
prefix = 'spam'
preRegex = re.compile(prefix)
dirs = os.listdir(os.getcwd())

preFiles = list(filter(preRegex.match, dirs))

numbers = []
numRegex = re.compile(r'\d+')
for item in preFiles:
    if numRegex.search(item) != None:
        numbers.append(numRegex.search(item).group(0))

numbers_sor = numbers.copy()
integer_map = map(int, numbers_sor)
integer_list = list(integer_map)
integer_list.sort()
integer_list2 = integer_list.copy()

for i in range(0, len(numbers)):
    if (i+1) not in integer_list2:
        shutil.copy(prefix + str(integer_list[i]).zfill(3) + '.txt', prefix + str(i+1).zfill(3) +'.txt')
        os.remove(prefix + str(integer_list[i]).zfill(3) + '.txt')
        integer_list2.remove(integer_list[i])
