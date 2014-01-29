from sys import argv

who = str(argv[1])

who_else = str(raw_input("who else?:"))

print "%s %s, smokes!" % (who, who_else)