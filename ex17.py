from sys import argv
from os.path import exists

script, from_file, to_file = argv

print "Copying from %s to %s" %(from_file, to_file)

#we could do these two in one line also. how?
input = open(from_file)
indata = input.read()

print "The input data is %d bytes long" %(len(indata))

#This piece of code just prompt the user before copying and hence is omitted

# print "Does the output file exist? %r" %(exists(to_file))
# print "Ready? Hit  RETURN to continue, CTRL-C to abort."
# raw_input()

output = open(to_file, "w")
output.write(indata)

print "Alright, we are done."