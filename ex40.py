#This defined a dictionary as shown
cities = {"CA": "San Fransisco", "MI": "Detroit", "FL": "Jacksonville"}

#Adding some more cities to the map: cities with refference to  their states
cities["NY"] = "New York"
cities["OR"] = "Portland"

prompt = "> "

#This is my defined finction that would add cities to the map
#if they already does not exit.
#morover it tells that functions can be passed as the return values but the ultimate return of the returned function
#would also get returned no matter what, and if nothing was there, ultimately "None" is gonna get printed
def not_found():
	print "Not found."
	print "Would You like to add one? (y/n): "
	response = raw_input(prompt)

	if response == "y":
		print "Enter the name of the city: " 
		cities[state] = raw_input(prompt)

	elif response == "n":
		print "Thank You for your response."
	else:
		print "Wrong choice. Interpretter should exit now"
		exit(0)

	return "Thank You!"

#This is the definition of the function that finds the cities from the map choosed
def find_city(map, state):
	if state in map:
		return map[state]
	else:
		return not_found()


#OK! pay attention now
#This is just tricky way of using the same function we defined above
#TBN: paranthesis are onnly required when you are calling the function. if u r just mingling around, you dont need those paranthesis
cities["_find"] = find_city



while True:
	print "(State? (Enter to Quit)",
	state = raw_input(prompt)

#This is a very important statement, It seems useless at first
#but it tells interpretter to exit if the user did not enter anything
	if not state: break

	#This line is the most important ever.. Study!!
	city_found = cities["_find"](cities, state)
	print city_found
