#functions, names, vars, code

# *args lets you use undefined number of args in functions
# aka puts all the args into a list

#this one is like your scripts wit argv
def print_two(*args):
    arg1, arg2 = args
    print "arg1: %r, arg2: %r" %(arg1,arg2)

# ok that *args is pointless, we can do this
def print_two_again(arg1,arg2):
    print "arg1: %r, arg2: %r" %(arg1,arg2)

#this takes just one argument
def print_one(arg1):
    print "arg1: %r" %arg1

def print_none():
    print "i got nothin"

print_two("zed","shaw")
print_two_again("zed","shaw")
print_one("first")
print_none()
