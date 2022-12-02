


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
    ip=''
    for line in data:
        line=line.strip()
        if 'Failed password for root from'  in line:
            #store the IP address if it is not already in the dictionary else increment the count
            ip=line.split(' ')[10]
            # print(ip)
            failed[ip]+=1
        elif 'Vagrantfile from' in line:
            # print(line)
            ip=line.split('from')[1].strip()
            if 'port' in ip:
                ip=ip.split('port')[0].strip()
            failed[ip]+=1

        elif 'Failed password for invalid user' in line:
            # print(line)
            ip=line.split('from')[1].split('port')[0].strip()
            failed[ip]+=1
        elif 'rhost' in line:
            ip=line.split('rhost=')[1].split(' ')[0]
            failed[ip]+=1
        elif 'Received disconnect from' in line:
            ip=line.split(' ')[8].split(':')[0]
            failed[ip]+=1
        elif 'Connection closed by' in line:
            ip=line.split(' ')[8]
            failed[ip]+=1

        elif 'Invalid user' in line:
            ip=line.split(' ')[9]
            failed[ip]+=1
        elif 'Did not receive identification string from' in line:
            ip=line.split(' ')[11]
            failed[ip]+=1
        elif 'Failed password for' in line:
            ip=line.split('from')[1].split('port')[0].strip()
            failed[ip]+=1

# remove the IP address from the dictionary if the count is less than 10
for ip in list(failed):
    if failed[ip] < 10:
        del failed[ip]
# print(failed)

            
failed=sorted(failed.items(), key=lambda x: x[1])
print("COUNT\t\t\tIP ADDRESS\t\tCOUNTRY")
for i in failed:
    country=geolite2.lookup(i[0])
    if country is not None:
        if len(i[0]) < 8:
            print(str(i[1]) + "\t\t\t" + i[0] + "\t\t\t" + country.country)
        elif len(i[0]) < 16:
            print(str(i[1]) + "\t\t\t" + i[0] + "\t\t" + country.country)