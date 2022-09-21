#!/usr/bin/env python3
##NAME : 
##Dont forget to chmod -x ping_test.py before running the file
import time
import os
import subprocess

os.system("clear")
while(True):
	
	ip_defaultgateway=subprocess.run(["ip","r" ] ,stdout=subprocess.PIPE)
	#output=> b'default via 10.0.2.2 dev .....' 
	ip_defaultgateway= str(ip_defaultgateway.stdout).split()[2]  #extracting the ip from output
	
	#pinging the ip to test if they work properly
	print("Pinging Gateway IP... "+ ip_defaultgateway)
	response_Gateway=subprocess.run(["ping", "-c", "1", ip_defaultgateway], stdout=subprocess.DEVNULL) #redirecting output for clean user interface
	#if return Address is 0 the test passted 
	if(response_Gateway.returncode==0): print(">Gateway test: Passed")
	else : print(">Gateway test: Failed")
	
	print("Pinging remote Ip... 129.21.3.17")
	response_remoteIp=subprocess.run(["ping", "-c", "1", "129.21.3.17"], stdout=subprocess.DEVNULL)
	#if return Address is 0 the test passted 
	if(response_remoteIp.returncode==0): print(">remoteIp test: Passed")
	else : print(">remoteIp test: Failed")
	
	
	print("Pinging DNS Address... google.com")
	response_remoteIp=subprocess.run(["ping", "-c", "1", "google.com"], stdout=subprocess.DEVNULL)
	#if return Address is 0 the test passted 
	if(response_remoteIp.returncode==0): print(">DNS test: Passed")
	else : print(">DNS test: Failed")
	
	print("Waiting! ctrl-c to exit...")
	print("=========================")
	time.sleep(2)

