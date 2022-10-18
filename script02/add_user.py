#!/usr/bin/python3

# import the necessary packages
import os
import sys
from collections import defaultdict
import re
import csv
Users=[]
# Read the CSV file
print('Adding new users to the system')
print("Please Note: The default password for new users is password")
print('For testing purposes, Change the password to 1$4pizz@')
with open('linux_users.csv', 'r') as f:
    reader = csv.reader(f)
    # check if the file is empty
    if os.stat('linux_users.csv').st_size == 0:
        print("The file is empty")
        sys.exit()
    # Skip the header row
    next(reader)
    for row in reader:
        # each row has EmployeeID,LastName,FirstName,Office,Phone,Department,Group,
        singleUser={}
        singleUser['EmployeeID']=row[0]
        singleUser['LastName']=row[1]
        singleUser['FirstName']=row[2]
        singleUser['Office']=row[3]
        singleUser['Phone']=row[4]
        singleUser['Department']=row[5]
        singleUser['Group']=row[6]

        # add only the users with complete information
        if singleUser['Group'] not in ['office','pubsafety']:
            print(f'The user {singleUser["EmployeeID"]} has invalid group')
            continue
        if singleUser['EmployeeID'] and singleUser['LastName'] and singleUser['FirstName'] and singleUser['Office'] and singleUser['Department'] and singleUser['Group']:
            Users.append(singleUser)
        else:
            print(f'The user {singleUser["EmployeeID"]} has insufficient data')
# add username column
for user in Users:
    user['UserName']=user['FirstName'][0]+user['LastName']
#convert to lowercase
for user in Users:
    user['UserName']=user['UserName'].lower()
# handle the spcial characters in the username
for user in Users:
    user['UserName']=re.sub('[^A-Za-z0-9]+', '', user['UserName'])
#handle duplicates by adding a number to the end of the username
li=[x['UserName'] for x in Users]
countdict={k:li.count(k) for k in li}
for k,v in countdict.items():
    if v>1:
        for user in Users:
            if user['UserName']==k:
                user['UserName']=user['UserName']+str(v)
                v-=1

# create the users

default_pass='password'
for row in Users:
    try:
        # create the user

        if row['Group'] == 'office':    # if the user is in office group
            shell='/bin/csh'    # set the shell to csh
        else:   # if the user is in other groups
            shell='/bin/bash'   # set the shell to bash
        print(f'Processing user {row["EmployeeID"]}',end='\t\t')
        # check if the group exists
        if not os.path.exists(f'/home/{row["Group"]}'):
            os.system(f'sudo groupadd {row["Group"]}')
            # create the home directory
            os.system(f'sudo mkdir /home/{row["Group"]}')   

        # check if the user exists
        if not os.path.exists(f'/home/{row["Group"]}/{row["UserName"]}'):
            # check if the directory exists
            if not os.path.exists(f'/home/{row["Group"]}/{row["UserName"]}'):
                os.system(f'sudo mkdir /home/{row["Group"]}/{row["UserName"]}')
            os.system('sudo useradd -d /home/' + row['Group'] + '/' +row['UserName'] + ' -g ' + row['Group']+ ' -s ' + shell + ' -p ' + default_pass + ' ' + row['UserName'])
            # # set  default password to expire after first login
            os.system('sudo chage -d 0 ' + row['UserName'])
            print(f'\t\tUser {row["EmployeeID"]} added')
        else:
            print(f'User {row["UserName"]} already exists')

    except Exception as e:
        
        print(e)