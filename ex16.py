## reading and writing files

#memorize these
    # close -- closes file
    # read -- read whole file
    # readline --reads just one line of file
    # truncate
    # write('stuff')
    # open -- defaults to read unless otherwise stated
# and the modifiers they can user_name
    # w,r,a, w+, r+, a+

from sys import argv

script, filename = argv

print " we're going to erase %r" % filename
print "if you don't want that, hit ctrl-c (^c)"
print "if you do want that, hit RETURN."

raw_input("?")

print " opening the file..."
# target is a file object that can be used with other read/write funcs
target = open(filename,'w')

# print "truncating the file... goodbye!"
# target.truncate()

print "now tell me three lines you want to type"
line1 = raw_input("line1:")
line2 = raw_input("line2:")
line3 = raw_input("line3:")

print "i'm going to write these to the file"

target.write(" %s \n %s \n %s \n" %(line1,line2,line3))


print " and finally we close the file"
target.close()
