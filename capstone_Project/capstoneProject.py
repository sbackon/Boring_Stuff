#!/usr/bin/env python3
# capstoneProject.py - Solves the first 5 Over the Wire Bandit levels on its own given proper configuration files.

import json, pwn, os, re

# If passwords.txt already exists, remove the file so wrong passwords are not used
if os.path.exists('passwords.txt'):
    os.remove('passwords.txt')



# Function which solves the level based on the commands in the .cfg files
def lvl_solver(json_file, txt_file, lvl):

    # Get information from the configuration file
    conf = open(json_file)
    variables = json.load(conf)
    conf.close()

    # Get password from passwords.txt (except for level 0)
    if lvl != 0:
        pass_file = open('passwords.txt', 'r')
        content = pass_file.readlines()
        passw = content[lvl-1].rstrip('\n')
        pass_file.close()
    else:
        passw = variables['password']

    # Informs the user which level one is currently in
    print('Entering Level ' + str(lvl) + ' ...')

    # Establish a connection to the Over the Wire Bandit server
    session1 = pwn.ssh(user=variables['username'], host=variables['address'], port=variables['port'], password=passw)
    io = session1.process('sh')

    # Execute commands from the .cfg file
    for key in variables['commands']:
        io.sendline(variables['commands'][key])

    # Get output of the password file
    pw1 = io.recvline(timeout=5).decode('utf-8')
    session1.close()

    # Store obtained password to file
    pw2 = re.search(r'\w+$\n', pw1)
    pwfile = open('passwords.txt', 'a+')
    pwfile.write(pw2.group())
    pwfile.close()



# Solve levels 0-5
lvl_solver('bandit1.cfg', 'passwords.txt', 0)
lvl_solver('bandit2.cfg', 'passwords.txt', 1)
lvl_solver('bandit3.cfg', 'passwords.txt', 2)
lvl_solver('bandit4.cfg', 'passwords.txt', 3)
lvl_solver('bandit5.cfg', 'passwords.txt', 4)
lvl_solver('bandit6.cfg', 'passwords.txt', 5)
