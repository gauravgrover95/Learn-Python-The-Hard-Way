x = "There are %d type of ppl" %10
binary = "binary"
do_not = "don't"
y = "Those who knows %s and those who %s" %(binary, do_not)

print ""
print ""
print x
print y

# %r gives us ability to replace it with anything, doesnt necesarily it has to be a string, integer or a float
print "I said: %r." %x
print "I also said: '%s'." %y

hilarious = False
joke_evaluation = "Isn't that joke so funny?! %r"

#focus on this part, this is important as it allows a developer to write same piece of string with different values according to the situation
print joke_evaluation % hilarious

w = "This is the left side of..."
e = "a string with the right side."

# "+" is used to concatinate strings
print w + e
