# more variable names

#formatters are %r, %s, %d. I don't really get them.
# they allow you to replace

my_name = 'michael saminsky'
my_age = 24
my_height = 74
my_weight = 180
my_eyes = 'blue'
my_teeth = 'white'
my_hair = 'brown'

print "lets talk about %s" %my_name
print "he's %d inches tall." %my_height
print "he's %s inches tall." %my_height
print "he's %d pounds heavy" % my_weight
print " actually thats not too heavy"
print " he's got %s eyes and %s hair" %(my_eyes, my_hair)
print " his teeth are usually %s depending on coffe" % my_teeth
print " if i add %d, %d, and %d, I get %s" % (my_age, my_height, my_weight, my_age+my_height+my_weight)

print "he's %s pounds heavy" % my_weight/3
