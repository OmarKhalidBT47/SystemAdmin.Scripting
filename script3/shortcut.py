#!/usr/bin/python3

import os
import sys
import time
# clear the screen
os.system('clear')
# print the current working directory
print('Current working directory: ', os.getcwd())
while True:
    # ask for input
    print('''
    ************************************************
	*************** Shortcut Creater ***************
	************************************************
    '''
    )
    print("""
    Enter Selection:

	1 - Create a shortcut in your home directory.
	2 - Remove a shortcut from your home directory.
	3 - Run shortcut report.""")

    option= input('Please enter a number (1-3) or q to quit: ')
    # if option 1 is selected
    if option == '1':
        # ask for file name to create shortcut
        file_name = input('Please enter the file name to create a shortcut: ')
        if os.path.isfile(file_name):
            # create a shortcut
            os.symlink(file_name, os.path.expanduser('~') + '/' + file_name)
            print('Creating Shortcut, please wait.')
            for i in range(0, 101, 5):
                sys.stdout.write("\r[%-20s] %d%%" % ('='*int(i/5), i))
                sys.stdout.flush()
                time.sleep(0.2)
            print('Shortcut created. Returning to Main Menu.')
            time.sleep(2)

    elif option == '2':
        filename = input('Please enter the shortcut/link to remove: ')
        if os.path.isfile(filename):
            if os.path.islink(filename):
                os.remove(filename)
                print('Removing Shortcut, please wait.')
                for i in range(0, 101, 5):
                    sys.stdout.write("\r[%-20s] %d%%" % ('='*int(i/5), i))
                    sys.stdout.flush()
                    time.sleep(0.2)
                print('Shortcut removed. Returning to Main Menu.')
                time.sleep(2)
            else:
                print('This is not a shortcut. Returning to Main Menu.')
                time.sleep(2)
        else:
            print('File does not exist. Returning to Main Menu.')
            time.sleep(2)

    elif option == '3':
        print('Generating Report. Please wait...')
        print('''
        	************************************************
            *************** Shortcut  Report ***************
            ************************************************
            ''')

        for i in range(0, 101, 5):
            sys.stdout.write("\r[%-20s] %d%%" % ('='*int(i/5), i))
            sys.stdout.flush()
            time.sleep(0.2)
        print('Your current directory is: ', os.getcwd())
        # The number of links is 
        # use the command find
        num_links = os.popen('find . -type l | wc -l').read()
        print('The number of links in this directory is: ', num_links)
        print("Symbolic link\t\t\t Target Path")
        # use the command find
        links = os.popen('find . -type l').read()
        # split the links
        links = links.split('\n')
        # remove the last element
        links.pop()
        for link in links:
            # use the command readlink
            target = os.popen('readlink ' + link).read()
            print(link, '\t\t\t', target)
        print('Report Generated. Returning to Main Menu.')
        time.sleep(2)

    elif option == 'q':
        print('Exiting Program. Goodbye.')
        time.sleep(2)
        break
    else:
        print('Please enter a valid option (1-3) or q to quit.')
        time.sleep(2)

print("Quiting the program. Returning to the shell.")
