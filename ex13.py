#Parameters, unpacking, and variables

#Awesome: argv allows you to put args right in command-line
#super important: how would you use this to make a
#command-line script?

from sys import argv

#in argv, first thing that's unpacked is script name (always??)
scrippity, blippity, second, third, fourth = argv

# x = raw_input("what's my name?")

print "The script is called:", scrippity
print "The first variable is called", blippity
print " the second var is called:", second
print " the third var is called:", third
print  "the raw input var is called:"
