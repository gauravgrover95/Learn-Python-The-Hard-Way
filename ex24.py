print "Let's practice everything"
print "You'd need to know about escapes with \\ tha do \n newlines and ]t tabs."

poem = """
\t The lovely world
with logic so firmly planted
cannot descern \n the needs of lovely
nor comprehend passion from intution
and requires an explaination
\n\t\t where there is none.
"""

print "---------------"
print poem
print "---------------"


five = 10 - 2 + 3 - 6
print "This should be five: %s" %(five)

#Ths function returns multiple values seperated by comma
#TBN: A function can return multiple values
def secret_formula(started):
	jelly_beans = started * 500
	jars = jelly_beans / 1000
	crates = jars / 100
	return jelly_beans, jars, crates

start_point = 10000
#this instruction unpacks the function returned values and give it to the following variables in order
beans, jars, crates = secret_formula(start_point)

print "with a starting point of: %d" %(start_point)
print "We'd have %d beans, %d jars, and %d crates." %(beans, jars, crates)

start_point /= 10

print "We can also do this way:"
#we can also fill the values of formatter through a function that provides multiple return values.
print "We'd have %d beans, %d jars, and %d crates." %(secret_formula(start_point))