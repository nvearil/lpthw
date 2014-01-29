from sys import argv

filename = argv[1]

file_object = open(filename)

print file_object.read()