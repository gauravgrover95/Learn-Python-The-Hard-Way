people = 30
cars = 40
buses = 15

if cars > people:
	print "We should take the cars"
elif cars < people:
	print "We should not take the cars"
else:
	print "We cannot decide"

if buses > cars:
	print "Thats too many buses"
elif buses < cars:
	print "May be we could take the buses"
else:
	print "We still cannot decide"

if people > buses:
	print "Alright lets take the buses"
else:
	print "Alright lets stay home then."