"""ex40.py - Modules,Classes, and Objects
   Class: LearnPythonTheHardway (Py2.7)
   Author: Michael Saminsky
   Date: 2017-08-22
"""
class Song(object):
    def __init__(self,lyrics):
        self.lyrics = lyrics

    def sing_me_a_song(self):
        for line in self.lyrics:
            print line

happy_bday = Song(['happy birthday to you',
                   'I don\'t want to be sued',
                   'So i\'ll stop right there'
                  ])

bulls_on_parade = Song(['they rally round the family',
                        'With pockets full of shells'
                       ])

happy_bday.sing_me_a_song()

bulls_on_parade.sing_me_a_song()
