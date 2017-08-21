"""ex33.py - excercise on While loops
   Class: LearnPythonTheHardway (Py2.7)
   Author: Michael Saminsky
   Date: 2017-08-21
"""
i = 0
numbers = []

while i < 6:
    print "At the top i is %d" % i
    numbers.append(i)
    i = i+1
    print "Numbers now: ", numbers
    print "At the bottom i is %d" % i

print "The numbers: "

for num in numbers:
    print num


# Change the above while loop into function that takes i as arg

def uselessIterator(iterateMeOnTheLips,skipFactor):
    """ This useless function prints you out a BUNCH of information that you
    definitely don't need. Takes an integer iterator as an argument!
    Have fun! """
    numbers = []
    i=0
    stupidHuman = ""
    print "Hello HUMAN would you prefer a for loop? or while loop?"
    while (stupidHuman not in ("for","while")):
        stupidHuman = raw_input("please type for or while: ")
        if stupidHuman not in ("for","while"):
            print "Abort. Shutdown. Stop that. Retry with the correct input."
    if stupidHuman == "while":
        while i < iterateMeOnTheLips:
            print "At the top i is %d" % i
            numbers.append(i)
            i = i+skipFactor
            print "Numbers now: ", numbers
            print "At the bottom i is %d" % i

        print "The numbers: "

        for num in numbers:
            print num
    elif stupidHuman == "for":
        for i in range(0,iterateMeOnTheLips,skipFactor):

            print "At the top i is %d" % i
            numbers.append(i)
            print "Numbers now: ", numbers
            print " At the bottom i is %d" % int(i+skipFactor)
        print "The numbers: "
        for num in numbers:
            print num
