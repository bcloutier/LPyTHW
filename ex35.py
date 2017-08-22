"""ex35.py - Branches and functions
   Class: LearnPythonTheHardway (Py2.7)
   Author: Michael Saminsky
   Date: 2017-08-22
"""

from sys import exit
import re

def gold_room():
    print "This room is full of gold. How much do you take?"

    choice = raw_input("> ")

    if re.search('[a-zA-Z]',choice): # if there's a letter, exit
        dead("Man, learn to type a number")
    if how_much < 50:
        print " Nice, you're not greedy, you have won"
        exit(0)
    else:
        dead("You greedy bastard.")

def bear_room():
    print "There is a bear here"
    print "The bear has a bunch of money."
    print "The fat bear is in front of another door."
    print "How are you going to move the bear?"
    bear_moved = False

    while True:
        choice = raw_input("> ")

        if choice == "take money":
            dead("The bear looks at you then slaps your face")
        elif choice == "taunt bear" and not bear_moved:
            print "The bear has moved from the door. You can go"\
                   " In there now."
            bear_moved = True
        elif choice == "taunt bear" and bear_moved:
            dead("The bear gets pissed off and chews your leg")
        elif choice == "open door" and bear_moved:
            gold_room()
        else:
            print "Try again, but les sstupid this time"

def cthulhu_room():
    print "Here is the evil Cthuluhu."
    print " If you kiss it on the lips, it'll spare your life"
    print " Do you flirt or run away?"

    choice =  raw_input("> ")

    if "flirt" in choice:
        start()
    elif "run" in choice:
        dead("Cthulhu so fast, you so fast die!")
    else:
        cthulhu_room(0)

def dead(why):
    print why, "too bad maybe later."
    exit(0)

def start():
    print "you're in a dark room."
    print "There is a door ro your right and left"
    print "Which one do you take?"

    choice = raw_input("> ")

    if choice == "left":
        bear_room()
    elif choice == "right":
        cthulhu_room()
    elif choice == "gold":
        gold_room()
    else:
        dead("You stumble around the room until you starve")

start()
