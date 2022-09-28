#!/usr/bin/env python3
##NAME : Omar Khalid Al Thani
##Dont forget to chmod -x ping_test.py before running the file

#colors in print
#red \033[91m
#green \033[92m 
#yellow \033[93m 
#None \033[00m 

import time
import os
import subprocess

os.system("clear")


while(True):
	print("\t\t*********************************")
	print("\t\t**********\033[92m  Ping tester \033[00m*********")
	print("\t\t*********************************")
	# Select option:
	# 0 - Quit
	# 1 - Display default Gateway; 
	# 2 - Run default Gateway Connectivity Test; 
	# 3 - Run Remote Connectivity Test; 
	# 4 - Run DNS Resolution Test.
	print("Selection:\n\n\t1 - Display default Gateway\n\t2 - Run default Gateway Connectivity Test\n\t3 - Run Remote Connectivity Test\n\t4 - Run DNS Resolution Test")
	print("Enter number \033[92m(1-4)\033[00m or \033[92m '0'\033[00m to quit the program.")
	
	notvalid=True
	while (notvalid):
		# select and enter a number between 1 t0 4.
		c= input("Select? ")
		if (not(c.isnumeric())):
			print("\033[91mInvalid input: Select from 1-4\033[00m")
			continue
		
		c=int(c)
		# clear the console if the input is between 1 to 4, otherwise shows error message and prompts user to select a number.
		if (c<5 and c>=0):
			notvalid=False
			os.system("clear")
		else:
			print("\033[91mInvalid input: Select from 1-4\033[00m")
	
	# input 0 - terminate process
	if (c==0):
		exit()

	# input 1 - display the default gateway.
	elif(c==1):
		# subprocess.run(["ip","r"]) to list all routes
		# save the output in ip_defaultgateway
		ip_defaultgateway=subprocess.run(["ip","r" ] ,stdout=subprocess.PIPE, stderr=subprocess.DEVNULL)
		# extracting the ip from output
		ip_defaultgateway= str(ip_defaultgateway.stdout).split()[2] 
		if(ip_defaultgateway=="virbr0"):
			print("\033[91mLink down... Please connect to a network\033[00m")
		
		else:print("your default gateway is \033[93m{}\033[00m".format(ip_defaultgateway))
	
	# input 2 - run the default gateway connectivity test
	# attempt to connect to the default gateway and see if it can establish a connection.
	elif(c==2):	
		print("Getting the default gateway..")
		ip_defaultgateway=subprocess.run(["ip","r" ] ,stdout=subprocess.PIPE)#stderr=subprocess.DEVNULL) #output=> b'default via 10.0.2.2 dev .....'
		ip_defaultgateway= str(ip_defaultgateway.stdout).split()[2] #extracting the ip from output
		if(ip_defaultgateway=="virbr0"):
			print("\033[91mLink down... Please connect to a network\033[00m")

		else:
			print("Pinging Gateway IP: \033[93m{}\033[00m".format(ip_defaultgateway))
			# ping the default gateway
			response_Gateway=subprocess.run(["ping", "-c", "1", ip_defaultgateway], stdout=subprocess.DEVNULL,stderr=subprocess.DEVNULL) #redirecting output for clean user interface,no errors
			# if return Address is 0 the test passed 
			if(response_Gateway.returncode==0): print("\033[92mGateway test Passed \033[00m")
			else : print("\033[91mGateway test Failed\033[00m")
	
	# input 3 - run remote connectivity test
	# attempt to connect with the specified IP address of the target computer and check for connectivity. 
	elif(c==3):
		# pinging the ip to test if they work properly
		# run a ping command on the remote IP address 129.21.3.17
		print("Pinging remote Ip: \033[93m129.21.3.17\033[00m")
		response_remoteIp=subprocess.run(["ping", "-c", "4", "129.21.3.17"], stdout=subprocess.DEVNULL,stderr=subprocess.DEVNULL)
		# if return Address is 0 the test passed 
		if(response_remoteIp.returncode==0): print("\033[92mRemoteIp test Passed \033[00m")
		else : print("\033[91mRemoteIp test Failed\033[00m") 
		
	# input 4 - run DNS resolution test
	# perform a lookup on an IP address	
	else:
		# run a ping command on 'google.com'
		print("Pinging DNS Address: \033[93mgoogle.com\033[00m")
		response_remoteIp=subprocess.run(["ping", "-c", "4", "google.com"], stdout=subprocess.DEVNULL,stderr=subprocess.DEVNULL)
		#if return Address is 0 the test passted 
		if(response_remoteIp.returncode==0): print("\033[92mDNS test Passed\033[00m")
		else : print("\033[91mDNS test Failed\033[00m")
		
	# waits for 2 seconds before clearing the screen	
	time.sleep(5)
	os.system("clear")