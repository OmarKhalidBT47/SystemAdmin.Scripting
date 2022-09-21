#!/usr/bin/env python3
##NAME : 
##Dont forget to chmod -x ping_test.py before running the file
##-> install netifaces if it isnt already installed
import time
import os
import subprocess
import netifaces

os.system("clear")

while(True):
	
	#using netifaces to find gateway ip
	url_ofdefaultgateway=netifaces.gateways()['default'][netifaces.AF_INET][0] #at time of testing it is 10.0.2.2
	
	#pinging the ip to test if they work properly
	print("Pinging Gateway IP... "+ url_ofdefaultgateway)
	response_Gateway=subprocess.run(["ping", "-c", "1", url_ofdefaultgateway], stdout=subprocess.DEVNULL) #redirecting output for clean user interface
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

