people = 20
cats = 30
dogs = 15

print ""
print ""
# Python expects you to indent something after you and a line with a : (colon).
if people < cats:
	print "Too many cats. the world is doomed"

if people > cats:
	print "Not many cats.. The world is saved"

if people < dogs:
	print "The world id drooled on!"

if people > dogs:
	print "The world is dry..."

dogs += 5

if people >= dogs:
	print "people are greater tha equal to dogs"

if people <= dogs:
	print "people are less than or equal to dogs"

if people == dogs:
	print "people are equal to dogs"
