#!/usr/bin/python

	#create a new file

fo = open("newfile.txt","w+")
print "File is opened\n"

	#Printing the file name

print "File name:- ", fo.name

	#Checking whether file is closed or not

#print "Closed? -> ", fo.closed

	#Writing a line in the file

fo.write("This is a new file created.\n")
print "\nA line is written in the file\n"


	#Closing the opened file

fo.close()
print "File is closed now"

#Read from the file
fo = open("newfile.txt","r+")
a = fo.read()
print "\nThe content of the file is as follows:\n\n", a

	#End
