from sys import argv
from os.path import exists

script, from_file, to_file = argv

print "Copying from %s to %s" % (from_file, to_file)

# we could do these on one line too, how?

indata = open(from_file).read()

# print "The input is %d bytes long" % len(indata)

# print "Does the output file exist? %r" % exists(to_file)
# print "Ready, hit RETURN to continue, or CTRL-C to abort."
# raw_input()

print "Copying %d bytes" % len(indata)

out_file = open(to_file, 'w')
out_file.write(indata)

print "Alright, done."

out_file.close()