# ex19 study drill

#write function that can be executed 10 different ways

# entering default var vals
def next_election(dem='obamy',rep='jegson',wildcard='trudeau'):
    print "your candidates are %s, %s, and a %s..." %(dem,rep,wildcard)
    print "how depressing"

#Study Drills

# 1. input from powershell
# dem = raw_input('who\'s your Democratic candidate?')
# rep = raw_input('who\'s your Republican candidate?')
# wildcard = raw_input('who\'s your wildcard candidate?')
# next_election(dem,rep,wildcard)

# 2. Use defaults
# next_election()

#3. ask for inputs in functoin cal
# next_election(raw_input('dem?'),raw_input('rep'),raw_input('wildcard?'))

#4. Ask for favorite letters and combine strings
# next_election(raw_input('vowel: ')+'rrie',
#  raw_input('consonant: ')+'arrie',raw_input('bird: ')+' faced-motherfucker')
#
# #5 enter regularstyle
# next_election('bird','tird','merd')

#6 fusion of raw input and previously called
next_election(raw_input('vowel: '),'light','fright')
