# import argv 
from sys import argv

# store argv[0] in script and argv[1] in filename
script, filename = argv

# store filename file object
txt = open(filename)

# return contents of file object and print them
print "Here's your file %r:" % filename
print txt.read()

print "Type the filename again:"
file_again = raw_input("> ")

txt_again = open(file_again)

print txt_again.read()