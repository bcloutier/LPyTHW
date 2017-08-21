## prompting and passing

# It is useful to set up a global var for your prompt string

from sys import argv

script, user_name,computersys = argv
prompt = '> '

print "Hi %s, I'm the %s script." %(user_name, script)
print "I'd like to ask you a few questions."
print "Do you like me %s?" % user_name
likes = raw_input(prompt)

print "where do you live %s?" % user_name
lives = raw_input(prompt)

print "What kind of computer do you have?"
computer = raw_input(prompt)
print " are you sure it's not %r?" % computersys
certainty = raw_input(prompt)

print """
Alright, so you said %r about liking me.
you live in %r. Not sure where that is.
and you have a %r computer. nice.
""" % (likes, lives, computer)
