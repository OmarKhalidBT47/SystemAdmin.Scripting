#!/usr/bin/python3


import os
import sys
import time
from collections import defaultdict
from geoip import geolite2
# clear the screen
os.system('clear')

# current time
now = time.strftime("%c")

print("Attacker Report - ", now)
failed=defaultdict(int)
with open('syslog.log', 'r') as f:
    data=f.readlines()
    # print(data)
    for line in data:
        line=line.strip()
        if 'Failed password for root from'  in line:
            #store the IP address if it is not already in the dictionary else increment the count
            ip=line.split(' ')[10]
            # print(ip)
            failed[ip]+=1
        elif 'Failed password for invalid user' in line:
            # print(line)
            ip=line.split('from')[1].split('port')[0].strip()
            # print(ip)
            failed[ip]+=1
# keep only attackers with more than 10 failed attempts
failed={k:v for k,v in failed.items() if v>=10}
failed=sorted(failed.items(), key=lambda x: x[1])
print("COUNT\t\t\tIP ADDRESS\t\tCOUNTRY")
for i in failed:
    country=geolite2.lookup(i[0])
    if country is not None:
        if len(i[0]) < 8:
            print(str(i[1]) + "\t\t\t" + i[0] + "\t\t\t" + country.country)
        elif len(i[0]) < 16:
            print(str(i[1]) + "\t\t\t" + i[0] + "\t\t" + country.country)