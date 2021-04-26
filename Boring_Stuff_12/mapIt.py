#!/usr/bin/env python3
# mapIt.py - Launches a map in the borwser using an address from the
# command line or clipboard.

import webbrowser, sys, pyperclip

if len(sys.argv) > 1:
    # Get address from command line
    address = ' '.join(sys.argv[1:])

else:
    # Get address from the clipboard
    address = pyperclip.paste()

webbrowser.open('http://www.google.com/maps/place/' + address)
