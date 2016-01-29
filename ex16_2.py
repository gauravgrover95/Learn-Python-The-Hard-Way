#This program reads the file we've created in ex16

from sys import argv

script, filename = argv

print script
print filename
print "Now we are going to read the file we've just created\n\n"

target = open(filename)
print target.read()