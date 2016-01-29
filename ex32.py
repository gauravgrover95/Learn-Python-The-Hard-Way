the_count = [1, 2, 3, 4, 5]
fruits = ["apples", "oranges", "pears", "apricots"]
change = [1, "pennies",2 , "dimes", 3, "quarters"]

#this first kind of for loop goes througha list
print ""
print ""
for number in the_count:
	print "This is the count " + str(number) 

print ""

#same as above
for fruit in fruits:
	print "A fruit of type %s" %(fruit)


print ""
#Also we can go through the mixed list too
#Notice we have to use %r, since we dont know what is in it
for i in change:
	print "I got %r" %(i)

#We can also buid lists, first start with an empty one
elements = []


print ""
#thn use the range functions to do 0 to 20 counts
for i in range (0,6):
	print "Adding %d to the list." %(i)
	# append is a function  that lists understand
	elements.append(i)

# Now we can print them out too
for i in elements:
	print "Element was %d" %(i)	

#***************************************************************************

# if we write a line and end it with a : (colon) then that
# tells Python to start a new block of code	