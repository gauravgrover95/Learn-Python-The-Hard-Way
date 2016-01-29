ten_things = "Apple Oranges Crow Telephones Light Sugar"

print ""
print ""
print "Wait there's not 10 things in that list, let's fix that."


#plz check below for some details
stuff = ten_things.split(" ")
more_stuff = ["Day", "Night", "Song", "Frisbee", "Corn", "Banana", "Girl", "Boy"]


#len function returns the length of the list or array
while len(stuff) != 10:
	next_one = more_stuff.pop()
	print "Adding: ", next_one
	stuff.append(next_one)
	print "There's %d items now" %(len(stuff))

print "There we go: ", stuff

print "Lets do some things with stuff."

print stuff[1]
print stuff[-1]
print stuff.pop()

#plz check below for some essential details...
print " ".join(stuff) #What? cooooolll..!!
print "#".join(stuff)


# len(...)
#     len(object) -> integer
    
#     Return the number of items of a sequence or mapping.
# (END)

# join(words, sep=' ')
#         join(list [,sep]) -> string
        
#         Return a string composed of the words in list, with
#         intervening occurrences of sep.  The default separator is a
#         single space.
        
#         (joinfields and join are synonymous)




# The point of this whole exercise was to teach you a thing essential to know abt what python does actually to the code written
# whenever we write something like: some_string.join(stuff) .. python actually searches for the join method
# within its own library and run the function as join(some_string, stuff)..
# So although it seems that only one argument was passed to join.
# but in actual, there were two arguments that were passed to the join method
# This is an essential information that is used while debugging the code.