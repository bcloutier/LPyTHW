
## files
#closing and opening files

from sys import argv

script, filename = argv
prompt = '>'
txt = open(filename)

print "here's your file %r" % filename
print txt.read()

print "Type the filename again:"
file_again = raw_input(prompt)

txt_again = open(file_again)

print txt_again.read()

#to close
txt.close()
txt_again.close()
