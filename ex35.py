from sys import exit

prompt = ("> ")

def gold_room():
	print "This room if full of gold. How much do you take?"

	next = raw_input(prompt)
	if "0" in next or "1" in next:
		how_much = int(next)

	else:
		dead("Man, learn to type a number.")

	if how_much < 50:
		print "Nice, you are not greedy, You Win!"
		exit(0)
	else:
		dead("You greedy bastard")

def bear_room():
	print "There is a bear in here."
	print "Bear has a bunch of honey"
	print "The fat bear is in front of another door"
	print "How are you going to move the bear?"
	bear_moved = False

	# print "1. Take the honey"

	while True:
		next = raw_input(prompt)

		if next == "take honey":
			dead("The bear looks at you and then pimp slaps your face off.")

		elif next == "taunt bear" and not(bear_moved):
			print "The bear has moved from the door. You can move through the door now."
			bear_moved = True	

		elif next == "taunt bear" and bear_moved:
			dead("The bear gets pissed off and chew your crotch off")
		elif next == "open door":
			gold_room()
		else:
			print "I got no idea what that means."

def cthulu_room():
	print "Here you see the great evil Cthulu."
	print "He, it, whatever stares at you and you go insane"
	print "Do you flee for your life or eat your head?"

	next = raw_input(prompt)

	if "flee" in next:
		start()
	elif "head" in next:
		dead("Well that was tasty!")
	else:
		cthulu_room()


def dead(why):
	print why, "Good Job!"
	exit(0)

def start():
	print "You are in a dark room."
	print "There is a door to your roght and left."
	print "Which one do you take?"

	next = raw_input(prompt)

	if next == "left":
		bear_room()
	elif next == "right":
		cthulu_room()
	else:
		dead("You stumble around the room until you starve to death.")

start()


#*******************************************
# exit(0) exits the interpretter whenever it is called and 0 indicates success, which is the default argument