"""ex39.py - Dictionaries
   Class: LearnPythonTheHardway (Py2.7)
   Author: Michael Saminsky
   Date: 2017-08-22
"""
# Lists have brackets around the object(s)
things = ['a','b','c','d']
print things[1]

# dicts have curly braces
stuff = {'name': 'Zed', 'age':39, 'height':6*12+2}
print stuff['name']
print stuff['height']
stuff['city'] = "San Francisco"
stuff[1] = "one!"
stuff[2] = sum([1,2,3,4])
print stuff[2]

#create a mapping of state to abbreviation
states = {
    'Oregon'    : 'OR',
    'Florida'   : 'FL',
    'California': 'CA',
    'New York'  : 'NY',
    'Michigan'  : 'MI'
    }
#Map cities to state abbrevs
cities = {
    'CA':'San Francisco',
    'MI':'Detroit',
    'FL':'Jacksonville'
}

#add a couple more state abbrevs
cities['NY'] = 'New York'
cities['OR'] = 'Portland'

# print out cities
print "-" * 10
print "NY State has: ", cities['NY']
print "Oregon has: ", cities['OR']

#Print some states
print "-" * 10
print "Oregon's abreviation is: ",states['Oregon']
print "Michigan's abbrevation is: ", states['Michigan']

#call the cities by using the states dicts
print "-" * 10
print "NY State has: ", cities[states['New York']]
print "Florida State has: ", cities[states['Florida']]

# print every state abbrevation
print "-" * 10
print "every state abbrevation:"
for abbrev,state in states.items():
    print "Abbreviation: %s, State: %s" % (abbrev,state)

# print every state Abbreviation
print "-" * 10
print "every city abbrevation:"
for abbrev,city in cities.items():
    print "Abbreviation is %s, City is %s" %(abbrev,city)

# Now both at the same time
print "-" * 10
print "both city and state at the same time::"
for state,abbrev in states.items():
    print "Abbreviation: %s, State: %s, City: %s." %(abbrev,state,cities[abbrev])
print "-" * 10
print "-" * 10

# now safely get abbreviation for a state that might not have it
state = states.get('Texas')
if not state:
    print "Sorry, no Texas."

#get a city with a default value
city = cities.get('TX','Does Not Exist')
print "They city for the state 'TX' is: ", city
