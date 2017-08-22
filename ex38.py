"""ex38.py - Doing things to lists
   Class: LearnPythonTheHardway (Py2.7)
   Author: Michael Saminsky
   Date: 2017-08-22
"""
import time

ten_things = "Apples Oranges Crows Telephone Hates Light"

print " Wait there are not 10 things in that list. let's fix that"

stuff = ten_things.split(' ')
more_stuff = ['day','night','song','frisbee','corn','banana','girl','boy']

while len(stuff) != 10:
    next_one = more_stuff.pop()
    print "adding: ", next_one
    stuff.append(next_one)
    print "there are %d items now" % len(stuff)

print "There we go, now we have: ", stuff
print "Let's do some stuff with the stuff"

print stuff[1]
print stuff[-1]
time.sleep(1)
print stuff.pop()
time.sleep(1)
print ' '.join(stuff)
time.sleep(1)
print '#'.join(stuff[3:5])
