# inputs and prompts

# learn more about functions:
# python.exe -m pydoc <funcName>

# again, %r is for debugging as it is raw representation
# and %s is for string/display

#prompts user with "Name?"
y = raw_input("Name?")

age = raw_input("How old are you?")
height = raw_input("What's your height?")
weight = raw_input("how fat you are????")

print "so you're %r old, %r tall, and %r fat." % (age,height, weight)


print "so you're %s old, %s tall, and %s fat." % (age,height, weight)
