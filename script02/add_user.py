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

#To open the file python has provided us open() built-in function 
#and open() function returns file object in our case it is named as 'f'
#by using this object f we can read the file.
with open('linux_users.csv', 'r') as f:
    reader = csv.reader(f)
    # check if the file is empty then print error message and safely exits from system
    if os.stat('linux_users.csv').st_size == 0:
        print("The file is empty")
        sys.exit()
    # Skip the header row
    next(reader)
    for row in reader:
        # each row has EmployeeID,LastName,FirstName,Office,Phone,Department,Group,
        # creating empty dictionary which will add 7 attribute listed above
        # for each user 
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

#setting default password as 'password'
default_pass='password'
for row in Users:
    try:
        #we are using try except handlers provided by python to deal with exception handling
        #so that if any type of exception occurs it will not throw exception
        #rather it takes the user-defined action explicitly define in except clause.
        
        # create the user
        if row['Group'] == 'office':    # if the user is in office group
            shell='/bin/csh'   
             # by using /bin/csh we are telling that we will use csh shell
             # as if we have a user who is in office group then the user 
             # must need interactive shell to enter commands
             # csh is a more interactive shell, it refers to C-shell and
             # used to enter commands interactively
        else:   # if the user is in other groups
            shell='/bin/bash' 
            # by using /bin/bash we are telling that we will use bash shell
            # as if we have a user who is not in office group then the user 
            # should not be able to enter commands via interactive shell
            # bash is a non-interactive shell , it also refers to C-shell and
            # used for controling OS without any need to navigate through the screens
        print(f'Processing user {row["EmployeeID"]}',end='\t\t')
        # check if the group exists
        if not os.path.exists(f'/home/{row["Group"]}'):
            #if the group doesn't exists then we will add group explicitly
            #by using groupadd command in linux followed by new group name
            os.system(f'sudo groupadd {row["Group"]}')
            # Also we are using mkdir linux based command to make a directory or folder
            # in a specified location in our case it is /home
            os.system(f'sudo mkdir /home/{row["Group"]}')   

        # check if the user exists
        if not os.path.exists(f'/home/{row["Group"]}/{row["UserName"]}'):
            # checking that if the UserName directory doesn't exists 
            # then we will create it using mkdir(i.e makedirectory) command
            if not os.path.exists(f'/home/{row["Group"]}/{row["UserName"]}'):
                os.system(f'sudo mkdir /home/{row["Group"]}/{row["UserName"]}')
            
            #also in an outer if we check that if user doesn't exists then we will
            # add a new user via useradd command which will add or create a new user 
            #with given credentials
            os.system('sudo useradd -d /home/' + row['Group'] + '/' +row['UserName'] + ' -g ' + row['Group']+ ' -s ' + shell + ' -p ' + default_pass + ' ' + row['UserName'])
            # set  default password to expire after first login
            # chage command is used to modify the password expiry date of the user's account
            #in every command we are using sudo because it grant administrator's privileges
            os.system('sudo chage -d 0 ' + row['UserName'])
            print(f'\t\tUser {row["EmployeeID"]} added')
        else: 
            print(f'User {row["UserName"]} already exists')

    except Exception as e:
        #catching any exception occured.
        print(e)