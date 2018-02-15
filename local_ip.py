#!/usr/bin/python
import os

# Get host name

hostname = os.popen("hostname").read()
hostname.replace("\n","")

print "\nThe host name is :- ",hostname


# Get local ip address

local_ip = os.popen("hostname -I").read()
local_ip.replace("\n","")

print "\nThe local ip address is :- ",local_ip
