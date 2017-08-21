"""
    ex26.py: this file contains a list of broken methods. The assignment is
    to correct these methods.
    Author: Mike Saminsky
    Date: 2017/08/21
"""

def break_words(stuff):
    """This function will break up words for us."""
    words = stuff.split(' ')
    #maybe should be () rather than (' ')
    return words

def sort_words(words):
    """Sorts the words."""
    return sorted(words)
        # mistake here..?

def print_first_word(words):
    #mistake no colon
    """Prints the first word after popping it off."""
    word = words.pop(0)
    print word
    #no  right parens, it should be pop not poop
    #totake first letter

def print_last_word(words):
    """Prints the last words after popping it off."""
    word = words.pop(-1)
    print word

def sort_sentence(sentence):
    """takes in a full sentence and rreturns the sorted words."""
    words = break_words(sentence)
    return sort_words(words)

def print_first_and_last(sentence):
    """Prints the first and last words of the sentence."""
    words = break_words(sentence)
    print_first_word(words)
    print_last_word(words)

def print_first_and_last_sorted(sentence):
    """Sorts the words then prints the first and last once."""
    words = sort_sentence(sentence)
    print_first_word(words)
    print_last_word(words)

print "Let's practice everything."
print 'You\'d need to know \'bout exapes with \\ that do \n newlines and \t tabs.'

poem = """
\t the lovely wolrd
with logic so firmly planted
cannot discern \n the needs of love
nor comprehend passion from intuition
and requires an explanation\n\t\twhere there is none.
"""

print "----------------"
print poem
print "----------------"

five = 10 - 2 + 3 - 5
print "this should be five: %s" % five

def secret_formula(started):
    jelly_beans = started * 500
    jars = jelly_beans / 1000
    crates = jars / 1000
    return jelly_beans, jars, crates

start_point = 10000
jelly_beans, jars, crates = secret_formula(start_point) #it's not taking these as vals

print "With a starting point of : %d" % start_point
print "We'd have %d jeans, %d jars, and %d crates." % (jelly_beans, jars, crates)

start_point = start_point/ 10

print " we can also do that this way:"
print "we'd have %d beans, %d jars, and %d crabapples." % secret_formula(start_point)

sentence = "All good things come to those who weight."

words = break_words(sentence)
sorted_words = sort_words(words)

print_first_word(words)
print_last_word(words)
print_first_word(sorted_words)
print_last_word(sorted_words)
sorted_words = sort_sentence(sentence)
print sorted_words

print_first_and_last(sentence)

print_first_and_last_sorted(sentence)
