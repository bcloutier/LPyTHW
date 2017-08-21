"""ex32.py - excercise on loops and lists
   Class: LearnPythonTheHardway (Py2.7)
   Author: Michael Saminsky
   Date: 2017-08-21
"""
# Storing data in lists
momSpaghettiLocations = ['plate','sweater','ocean']
dadSpaghettiLocations = ['Not Available','Dads don\'t make spaghetti']
volumeSpaghetti = ['3','9','100']

the_count = [1,2,3,4,5]
fruits = ['apples','different_apples','same_apples_as_initially']
change = [1,'pennies',2,'dimes',3,'quarters']

for number in the_count:
    print "This is count %d"% number

for fruit in fruits:
    print "A fruit of type: %s" % fruit

# Lists can be mixed numbers and string
for i in change:
    print "I got %r" % i

# Building lists
elements = []

# Then using range function to do 0-5 counts
for i in range(0,6):
    print " adding %d to the list" %i
    elements.append(i)
print elements
