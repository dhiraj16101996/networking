#!/usr/bin/python
import os

# Create a directory
os.mkdir("newdir")
print "\n A new directory with the name newdir is created \n"

# Change directory
os.chdir("/root/Desktop/.python_learn/newdir")
print "\nThe directory has been changed\n"

# Check the current working directory

current_working_dir = os.getcwd()
print "\n The current working directory is --> "+current_working_dir+"\n"

os.chdir("/root/Desktop/.python_learn")


# Delete a directory

os.rmdir("/root/Desktop/.python_learn/newdir")
print "\nThe directory is deleted\n"
