#!/usr/bin/python
import os

# Finding Gateway ip using route command

gateway = os.popen("ip route show").read()
gateway.replace("\n","")
gateway = gateway[11:23]
print gateway
