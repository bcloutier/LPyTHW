# more Printing

#Booleans always capitalized (false != False)


formatter = "%s %r %r %r"

print formatter % (1,2,007,4)
print formatter % ("one", "two","three","four")
print formatter % (True, False, False, True)
print formatter % (formatter, formatter, formatter, formatter)
print formatter % (
    "I had this thing.",
    "that you could type up right.",
    "but it didn't sing.",
    "so i said goodnight."
)
