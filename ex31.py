prompt = "> "
print "You enter a dark room with two doors. Do you go through door #1 or door #2?"

door = raw_input(prompt)

if door == "1":
	print "There's a giant bear here eating a cheese cake. What do you do?"
	print "1. Take the cake"
	print "2. Scream at the bear"

	bear = raw_input(prompt)

	if bear == "1":
		print "The bear eats your face off. Good Job!"
	elif bear == "2":
		print "The bear eats your legs off. Good Job!"
	else:
		print "Well doing %s is probably better. The bear runs away!" %(bear)

elif door == "2":
	print "You stare into the endless abyss at Cthuhlu's retina."
	print "1. Blueberries"
	print "2. Yellow jacket clothespin"
	print "3. Understanding revolvers yelling melodies."

	insanity = raw_input(prompt)

	if insanity == "1" or insanity == "2":
		print "Your body survives powdered by mind of jellow. Good Job!"
	else:
		print "the insanity rots your eyes into a pool of muck. Good Job!"

else:
	print "You stumble around and fall on the knife and die. Good Job!"