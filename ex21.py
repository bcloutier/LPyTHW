# functions can return something

def add(a, b):
    print "COMPUTING SUM %d + %d" % (a,b)
    return a + b

def subtract(a,b):
    print "COMPUTING MINUSY THING %d - %d" % (a,b)
    return a - b

def multiply(a,b):
    print "COMPUTING PRODUCT OF %d x %d" % (a,b)
    return a * b

def divide(a,b):
    print " COMPUTING QUOTIENT OF %d / %d" % (a,b)
    return a / b

print "time to do some math, bitches!"

age = add(30,5)
height = subtract(78,4)
weight = multiply(90,2)
iq = divide(100,2)

print "Age: %d, height: %d, weight: %d, iq: %d" %(age, height, weight, iq)

# a puzzle for extra credit, type it in anyway
print " here is a puzzle."

what = add(age, subtract(height, multiply(weight,divide(iq,2))))

print " that becomes: ", what, "Can you do that by hand?"
