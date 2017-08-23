#chaining functions with "."
mode = "ELELE"
mode.lower() # puts mode into function lower() >> "elele"
mode.lower().startswith('e')

#if else statements
if condition:
    response
elif condition:
    response
else:
    blah

#Cool functions
foo.lower() -> will lowercase foo


## naming conventions
    # two leading underscores in a name let the interpreter know to replace
    # the name with "_classname_foo"
    # In example below, __init__ would get interpreted as _classFoo__init
    class classFoo:
        def __init__():
            print yes
 # A file named __init__.py must exist in every directory that should be
#   treated as a package
