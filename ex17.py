#file stuff

#practice chaining file objects and read/write functions

#unclear: why when i run echo in powershell to create a txt file
# does it add weird unicode character at end?

# attempt at shortest version of code below
from sys import argv
from os.path import exists

script, from_file, to_file = argv

print("It is %r that the output file exists.") %exists(to_file)
print "Do you want to copy %s to %s?" %(from_file,to_file)
raw_input("ctrl-c to cancel, hit enter to continue")

infile = open(from_file)
indata = infile.read()
print indata
open(to_file,'w').write(indata)






# from sys import argv
# from os.path import exists
#
# script, from_file, to_file = argv
#
# print " copying from %s to %s" %(from_file,to_file)
#
# # read the opened file object in one line!
# indata = open(from_file).read()
# # in_file = open(from_file, 'r')
#
# print "the input file is %d bytes long" %len(indata)
#
# print " does the output file exist? %r" % exists(to_file)
# print "ready, hit RETURN to continue or CTRL-C to abort"
# raw_input()
#
# out_file = open(to_file, 'w')
# out_file.write(indata)
#
# print "alrighty then"
#
# out_file.close()
#
