"""
    ex25.py: contains methods for parsing and manipulating strings.
    Author: Mike Saminsky
    Date: 08/21/2017 """


def break_words(stuff):
    """This Function will make break up words for us. """
    words = stuff.split(' ')
    return words

def sort_words(words):
    """This function murders a small child at random
    \n also sorts the words... possibly alphabetically.
    """
    return sorted(words)

def print_first_word(words):
    """Prints the first word after popping it off."""
    word = words.pop(0)
    print word

def print_last_word(words):
    """Prints the last word after popping it off."""
    word = words.pop(-1)
    print word

def sort_sentence(sentence):
    """this little man takes a full sentence and returns the sorted
    words.
    """
    words = break_words(sentence)
    return sort_words(words)

def print_first_and_last(sentence):
    """This function does nothing at all
    oh wait fuck y'all it actually prints the first and last words
    \n suck it.
    """
    words = break_words(sentence)
    print print_first_word(words)
    print print_last_word(words)

def print_first_and_last_sorted(sentence):
    """takes a sentence, sorts it, prints first and last word.
    \nkapeesh?
    \ncaprese?
    """
    words = sort_sentence(sentence)
    print_first_word(words)
    print_last_word(words)
