


print "Let's practice everything."
print 'You\'d need to know \'bout escapes with  \\ that do \n new lines and \t tabs.'

poem = """
\tThe lovely world
with logic so firmly planted
cannot discern \n the needs of love
nor comprehend passion from intuition
and requires an explanation
\n\t\twhere there is none.
"""

print "------------"
print poem
print "------------"

five = 10 - 2 + 3 - 6
print "This should be five: %s" % five

def secretFormula(initBeans):
    """This function returns number of jelly beans, jars, and crates,
        given an initial number of beans to start. """
    jelly_beans = initBeans * 500
    jars = jelly_beans / 1000
    crates = jars / 100
    return jelly_beans, jars, crates

start_point = 10000
beans, jars, crates = secretFormula(start_point)

print "With a starting point of: %d" % start_point
print " We'd have %d beans, %d jars, and %d crates." % (beans, jars, crates)

start_point = start_point / 10

print "We can also do that this way:"
print " We'd have %d beans, %d jars, and %d crates" % secretFormula(start_point)
