"""ex36.py - Designing and Debugging
   Class: LearnPythonTheHardway (Py2.7)
   Author: Michael Saminsky
   Date: 2017-08-22
"""
import re
import time

def begin():
    print " Greetings WORM."
    print " You have been accepted to the most prestiguous startup incubator"\
          " in the world: eStartup2000.biz. I started it because I wanted to"\
          " radically change the world. For the better."
    print " Before we begin, I want to know about why you've decided to join"\
          " our family."
    print " Why did you decide to join our family here at eStartup2000.biz?"

    reason = raw_input("> ")

    print " That's the dumbest thing I've heard all morning. I hate your wormy"\
          " words."
    time.sleep(1)
    print " I also need to know your age. We don't discriminate based on age,"\
          " it's for our own internal demographic information."
    print " How old are you?"

    age   = raw_input("> ")
    ageIsString = re.search('[a-zA-Z]',age)

    if ageIsString:
        print "If you can't type numbers, how are you planning"\
              " to start a startup? Startups are just glorified number typing"\
              " companies! We're calculators with glasses and gourds of mate."\
              " Get out of my office and never look anyone in the eyes again."
        booted()
    elif int(age) > 12:
        print "Are you Ashton Kutcher and are you Punk`d'ing me?"
        print "I have never met anyone who is", age, "years old. Much too old."
        print "My only advice to you is to contract that Benjamin Buttons"\
              " disease. Good luck."
        booted()
    else:
        print "I won't lie to you, you're probably too old to be here. But "\
              "we'll give it a try."

    productMarketFit()


def productMarketFit():
    i = 0
    q = ["are you ready?", "What's your product?",
                 "What's your market?","If you could eat human flesh and get"\
                 " away with it... would you?"]
    qNa = {q[0]:"You bet your slappy hams I'm ready. Hollywood here I come!",
           q[1]:"Snake Eggs", q[2]:"Hob Goblins",q[3]:"absolutely yes"}
    print "OKAY fine, you've made it to the first trial, WORM. Are"\
          " you ready?"
    while i < 5:
        choice = raw_input("> ")
        if choice != qNa[q[0]]:
            print "I don't know what you mean by that you decomposer."\
                  " ARE YOU READY?"
            i += 1
            #print qNa[q[0]]
            if i == 2:
                print "WHY CAN'T YOU JUST SAY", qNa[q[0]],"like a normal child?"
        else:
            i=5

    print "Pathetic. Next question. There are no wrong answers. %s" % q[1]
    i=0

    while i < 5:
        choice = raw_input("> ")
        if choice != qNa[q[1]]:
            print "Wrong. Also a little racist. %s" % q[1]
            i += 1
            if i == 2:
                print "I wish you would say something like: ", qNa[q[1]]
        else:
            i=5

    print "Hmmm... maybe you're not as segmented an annelid as I once thought."\
          " I myself have been thinking there could be a sizable demand for"\
          ,qNa[q[1]]
    print "Well Dr. Worm, %s" % q[2]
    i = 0

    while i < 5:
        choice = raw_input("> ")
        if choice != qNa[q[2]]:
            print "I said %s Not 'What can you say that will immediately di"\
                  "sappoint everyone you've ever known or have yet to meet?'"% q[2]
            i += 1
            if i == 2:
                print "I wish you would say something like: ", qNa[q[2]]
        else:
            i=5

    print "Yes... %s Are you a growing demographic with more and more expendable"\
          " income..." % qNa[q[2]]
    print "Final Question. This ones stays between us. No wrong answers: %s"%q[3]
    i = 0

    while i < 5:
        choice = raw_input("> ")
        if choice != qNa[q[3]]:
            print "Don't be ashamed. Don't be afraid. Just tell the truth:"\
                  " %s" % q[3]
            i += 1
            if i == 2:
                print "If I was in your wormy cuticle I'd just admit it and"\
                      " say:", qNa[q[3]]
        else:
            i=5

    #print ""
#     choice = raw_input("> ")
#     if :
#
#     elif:
#
#     else:
#
# def noveltyWearingOff():
#     print ""
#     print ""
#     print ""
#     print ""
#     choice = raw_input("> ")
#     if :
#
#     elif:
#
#     else:
#
# def troughOfSorrow():
#     print ""
#     print ""
#     print ""
#     print ""
#     choice = raw_input("> ")
#     if :
#
#     elif:
#
#     else:
#
def booted():
    print "You've been kicked out. Git. Go on now, git."
    exit(0)
