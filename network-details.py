#!/usr/bin/python
import os
from time import sleep


# Finding network interface
def network_interface():
	route = os.popen("route -n").read()
	route.replace("\n","")
	network = "wlan0"
	if "eth0" in route:
		network = "eth0"
	elif "wlan1" in route:
		network = "wlan1"
	print "\n\nNetwork interface :- ", network


# Finding network it is connected to
def network_name():
	name = os.popen("iwgetid -r").read()
	name = name.replace("\n","")
	print "Wireless Network name :- ", name


# Finding hostname
def hostname():
	host = os.popen("hostname").read()
	host = host.replace("\n","")
	print "Host name :- ", host


# Finding local ip address
def local_ip():
	ip = os.popen("hostname -I").read()
	ip = ip.replace("\n","")
	print "Local ip :- ", ip


# Finding default gateway
def gateway():
	gate = os.popen("ip route show").read()
	gate = gate.replace("\n","")
	print "Gateway :- ", gate[11:23]

# Main function to run
def main():
	print "Finding Network interface.............."
	sleep(2)
	print "Network interface found"
	sleep(1)
	print "Finding Network name with which this device is connected........"
	sleep(2)
	print "Network name found"
	sleep(1)
	print "Finding hostname......."
	sleep(2)
	print "Hostname found"
	sleep(1)
	print "Finding local ip........"
	sleep(2)
	print "Local ip found"
	sleep(1)
	print "Finding default gateway.........."
	sleep(2)
	print "Gateway found"
	sleep(1)
	network_interface()
	network_name()
	hostname()
	local_ip()
	gateway()
main()
