#escape sequences

#memorize list below!

helpy = "help\f"
tabby_cat = "\t I'm tabbed in"
persion_cat = "I'm split\non a line."
backslash_cat = "I'm \\ a \\ real\\ prick."

fat_cat = """
I'll do a list:
\t- Cat food
\t* Fishies
\t* Catnip\n\t* Grass
"""
print helpy
print tabby_cat
print persion_cat
print backslash_cat
print fat_cat


# List of escapes
# \\  backslash (\)
# \'  single quotes
# \"  double-quotes
# \a ascii bell (BEL)
# \b ascii backspace (BS)
# \f ASCII formfeed (FF)
# \n ASCII linefeed (LF)
# \N{name}   character named name in the unicode database
# \r Carriage return
# \t horizontal tab
# \uxxxx character with 16-bit hex val xxxx (u''string only)
# \Uxxxxxxxx character with 32-bit hex val xxxxxxxx (u'' string only)
# \v ASCII vertical tab
# \ooo character with octal value ooo
# \xhh character with hex value hh
