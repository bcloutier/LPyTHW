"""
    ex29.py: Practicing if statements
        Author: Mike Saminsky
        Date: 2017/08/21
"""
#Set-up vars
earthHours = 1000000
passionProjects = 500
practiceHours = 10000

if passionProjects*practiceHours <earthHours:
    print " You don't have time to accomplish everything you want to accomplish!"
if passionProjects*practiceHours >earthHours:
    print "Hooray you have plenty of time!"
earthHoursNew = 5*earthHours
print "\nadding %d hours to life simulation...\n" % (earthHoursNew - earthHours)
if passionProjects*practiceHours == earthHoursNew:
    print "Oh Crumbles, it's going to be tight!"
