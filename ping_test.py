#!/usr/bin/env python3
##NAME : 
##Dont forget to chmod -x ping_test.py before running the file

#colors in pring 
#red \033[91m
#green \033[92m 
#yello \033[93m 
#None \033[00m 

import time
import os
import subprocess

os.system("clear")


while(True):
	print("\t\t*********************************")
	print("\t\t**********\033[92m  Ping tester \033[00m*********")
	print("\t\t*********************************")
	
	print("Selection:\n\n\t1 - Display default Gateway\n\t2 - Run default Gateway Connectivity Test\n\t3 - Run Remote Connectivity Test\n\t4 - Run DNS Resolution Test")
	print("Enter number \033[92m(1-4)\033[00m or \033[92m '0'\033[00m to quit the program.")
	
	notvalid=True
	while (notvalid):
		c= input("Select? ")
		if (not(c.isnumeric())):
			print("\033[91mInvalid input: Select from 1-4\033[00m")
			continue
		
		c=int(c)
		if (c<5 and c>=0):
			notvalid=False
			os.system("clear")
		else:
			print("\033[91mInvalid input: Select from 1-4\033[00m")
	
	if (c==0):
		exit()
	elif(c==1):
		ip_defaultgateway=subprocess.run(["ip","r" ] ,stdout=subprocess.PIPE, stderr=subprocess.DEVNULL)	
		ip_defaultgateway= str(ip_defaultgateway.stdout).split()[2] 
		if(ip_defaultgateway=="virbr0"):
			print("\033[91mLink down... Please connect to a network\033[00m")
		
		else:print("your default gateway is \033[93m{}\033[00m".format(ip_defaultgateway))
		
	elif(c==2):	
		print("Getting the default gateway..")
		ip_defaultgateway=subprocess.run(["ip","r" ] ,stdout=subprocess.PIPE)#stderr=subprocess.DEVNULL) #output=> b'default via 10.0.2.2 dev .....'
		ip_defaultgateway= str(ip_defaultgateway.stdout).split()[2] #extracting the ip from output
		if(ip_defaultgateway=="virbr0"):
			print("\033[91mLink down... Please connect to a network\033[00m")

		else:
			print("Pinging Gateway IP: \033[93m{}\033[00m".format(ip_defaultgateway))
			response_Gateway=subprocess.run(["ping", "-c", "1", ip_defaultgateway], stdout=subprocess.DEVNULL,stderr=subprocess.DEVNULL) #redirecting output for clean user interface,no errors
			#if return Address is 0 the test passted 
			if(response_Gateway.returncode==0): print("\033[92mGateway test Passed \033[00m")
			else : print("\033[91mGateway test Failed\033[00m")
		 
	elif(c==3):
		#pinging the ip to test if they work properly
		print("Pinging remote Ip: \033[93m129.21.3.17\033[00m")
		response_remoteIp=subprocess.run(["ping", "-c", "1", "129.21.3.17"], stdout=subprocess.DEVNULL,stderr=subprocess.DEVNULL)
		#if return Address is 0 the test passted 
		if(response_remoteIp.returncode==0): print("\033[92mRemoteIp test Passed \033[00m")
		else : print("\033[91mRemoteIp test Failed\033[00m") 
		
		
	else:
		print("Pinging DNS Address: \033[93mgoogle.com\033[00m")
		response_remoteIp=subprocess.run(["ping", "-c", "1", "google.com"], stdout=subprocess.DEVNULL,stderr=subprocess.DEVNULL)
		#if return Address is 0 the test passted 
		if(response_remoteIp.returncode==0): print("\033[92mDNS test Passed\033[00m")
		else : print("\033[91mDNS test Failed\033[00m")
		
	
	time.sleep(2)
	os.system("clear")
