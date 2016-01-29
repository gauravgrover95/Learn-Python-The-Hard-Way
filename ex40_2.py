#This program demonstrates for loop for dictionaries
#for each loop only fetches the element name, and not the element details.
#for details you have to use loop as demonstrated in this program's code

#This defined a dictionary as shown
cities = {"CA": "San Fransisco", "MI": "Detroit", "FL": "Jacksonville"}

#Adding some more cities to the map: cities with refference to  their states
cities["NY"] = "New York"
cities["OR"] = "Portland"

for Name in cities:
	print "Here is the element you have been finding: ", cities[Name]