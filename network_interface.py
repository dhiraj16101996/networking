#!/usr/bin/python
import os

# Storing the output of route
route = os.popen("route -n").read()
route.replace("\n","")

#finding the network interface now
network_interface = "wlan0"
if "eth0" in route:
	network_interface = "eth0"
elif "wlan1" in route:
	network_interface = "wlan1"

print network_interface
