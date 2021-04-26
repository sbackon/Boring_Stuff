#!/usr/bin/env python3
# madLips.py - python3 madLips.py <path of textfile> opens a textfile and lets user
#               change the words ADJECTIVE, NOUN, ADVERB and  VERB with user input

import sys, os, re
from pathlib import Path

# File to read and alter
if Path(sys.argv[1]).is_absolute():
    textFilePath = Path(sys.argv[1])
else:
    textFilePath = Path.cwd() / sys.argv[1]

if not textFilePath.is_file():
    print('Specified file path  does not exist.')

# Read file
textString = textFilePath.read_text()

# Search for adjectives, nouns and verbs in the string
adjRegex = re.compile(r'ADJECTIVE|NOUN|VERB')
while adjRegex.search(textString) != None:
    entered = input('Please enter a ' + adjRegex.search(textString).group() + ': \n')
    textString = adjRegex.sub(entered, textString, 1)

# Save to new file
newText = open('alterd.txt', 'w')
newText.write(textString)
newText.close()

