"""
    ex31.py: Practice using conditionals to make decisions,
             based on user inputs.
    OrigSource: LearnPythonTheHardway
    Author: Michael Saminsky
    Date: 2017-08-21
"""
print "You enter a dark room with two doors. Do you go through door #1 or door #2?"

door = raw_input("> ")

if door == '1':
    print "You open the door, and almost immediately encounter a medium-sized"\
          " man in a\nbear costume who begins to gnaw your leg."\
          " What do you do? \n"\
          "1. Pull your leg away. \n"\
          "2. Scream at the bear. \n" \
          "3. Begin to gnaw the bear's leg."
    bear = raw_input("> ")

    if bear == '1':
        print "The bear looks you in the eyes and begins to scream its true "\
              "name, over and over.\nYou die from embarassment."
    elif bear == '2':
        print "Your screams stun the bear. The lights come on and you find "\
                 "yourself in a packed library with signs hanging \non all the "\
                 "walls stating that yelling at the bear is expressly "\
                 " forbidden.\nYou are shamed out of existence by the bear,"\
                 " the library-goers, and the librarian."
    elif bear == '3':
        print "The bear writhes in ecstacy. Your power play has backfired.\n"\
              "You and the bear continue to gnaw at each other until you "\
              "are no more."
    else:
        print "You do nothing, and lose your leg. Nice one, coward."
elif door == '2':
    print "There you are, face-to-face with your middle school crush, "\
             "Lauren Bass! Her face is just as you remember it,\nand her legs "\
             "have been replaced with six mechanized spider legs, like from "\
             "Wild Wild West.\nShe touches one of her legs to your lips, and "\
             "asks you to slow dance. You hesitate, and she pulls a\nberretta "\
             "m9 out from behind her with one of her other mechanized legs.\n"\
             "1. Bide your time until her spider legs rust.\n"\
             "2. Seduce her with your dance moves, and fulfill both your\n"\
             "   middle school fantasies of slow-dancing to R. Kelly.\n"\
             "3. Pull out your berretta m9 and blow her wicked webs to bits.\n"
    lauren = raw_input("> ")
    if lauren == "1":
        print "You and Lauren grow impatient waiting for her legs to rust.\n"\
                "She begins to wrap you in a web extruding from her thorax "\
                "as you fidget\nwith your fidget spinner, waiting for the end."\
                "\nJust as mother had predicted."
    elif lauren == "2":
        print "You marry Lauren, and raise thousands of healthy spiders."
    elif lauren =="3":
        print "You're a crap shot, just as mother told you. You waste all "\
               "your bullets shooting around Lauren. \nShe blows your wicked "\
               "webs to bits."
    else:
        print "Your total inaction is very awkward! Lauren slowly moves "\
                  "backs away into what looks like a large, dusty, spider "\
                  "cup."
else:
    print "how did you know about door %r?"%door
    print "That door contains a room of absolute nightmares."
    print "I won't accompany you for that journey, friend."
