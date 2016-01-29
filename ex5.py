name = "Gaurav Grover"
age = 20
height = 172 #centimeters
weight = 80 #kgs
teeth = "white"
eyes = "black"
hair = "black"

print ""
print ""

#2. Try more format characters. %r is a very useful one, it’s like saying “print this no matter what”.
print "lets talk about %r" % name

print "He's %d cms tall" % height
print "He has a weight of %d kgs" %  weight
print "Actually thats not too heavy"
print "he's got %s eyes and %s hair" %(eyes, hair)
print "his teeth are usually %s depending on the coffee" %(teeth)

#this line is tricky, try to get it exactly right
print "if i add %d, %d and %d, I get %d" %(age, height, weight, age + height + weight)

#4. Try to write some variables that convert the inches and pounds to centimeters and kilos. Don’t just type in the
# measurements, but work out the math in Python.