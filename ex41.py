from sys import exit
from random import randint

prompt = "> "

def death():
	quips = ["You dies, you kinda suck at this game.", 
			 "Your mom would be proud, if she were smarter.",
			 "Scuh a loser.",
			 "I've a small puppy that is better at this."]

#randint is a function that gives out random integer between the range provided(including limits of range)
	print quips[randint(0, len(quips) - 1)]
	exit(1)

def princess_lives_here():
	print "You see a beautiful princess with a shiny crown."
	print "She offers you some cake."

	eat_it = raw_input(prompt)

	if eat_it == "eat it":
		print "You explode like a pinata full of frogs."
		print "Princess cackles and eat the frogs.. Yum!"
		return "death"

	elif eat_it == "do not eat it":
		print "She throws the cake at you and cuts off your head."
		print "The last thing you see is her munching on your torso. Yum!"
		return "death"

	elif eat_it == "make her eat it":
		print "The Princess screams as you cram the cake in her mouth."
		print "Then she smiles and cries and thanks you for saving her."
		print "She points to a tiny door and says, 'The Koi needs cake too.'"
		print "She gives you the very last bit of cake and shoves you in."
		return 'gold_koi_pond'
	else:
		print "The princess looks at you confused and just points at the cake."
		return 'princess_lives_here'

def gold_koi_pond():
	print "There is a garden with a koi pond in the center."
	print "You walk close and see a massive fin poke out."
	print "You peek in and a creepy looking huge Koi stares at you."
	print "It opens its mouth waiting for food."

	feed_it = raw_input(prompt)

	if feed_it == "feed it":
		print "The Koi jumps up, and rather than eating the cake, eats your arm."
		print "You fall in and the Koi shrugs than eats you."
		print "You are then pooped out sometime later."
		return 'death'

	elif feed_it == "do not feed it":
		print "The Koi grimaces, then thrashes around for a second."
		print "It rushes to the other end of the pond, braces against the wall..."
		print "then it *lunges* out of the water, up in the air and over your"
		print "entire body, cake and all."
		print "You are then pooped out a week later."
		return 'death'

	elif feed_it == "throw it in":
		print "The Koi wiggles, then leaps into the air to eat the cake."
		print "You can see it's happy, it then grunts, thrashes..."
		print "and finally rolls over and poops a magic diamond into the air"
		print "at your feet."

		return "bear_with_sword"

	else:
		print "The koi gets annoyed and wiggles a bit."
		return "gold_koi_pond"

def bear_with_sword():
	print "Puzzled, you are about to pick up the fish poop diamond when"
	print "a bear bearing a load bearing sword walks in."
	print '"Hey! That\' my diamond! Where\'d you get that!?"'
	print "It holds its paw out and looks at you."

	give_it = raw_input(prompt)

	if give_it == "give it":
		print "The bear swipes at your hand to grab the diamond and"
		print "rips your hand off in the process. It then looks at"
		print 'your bloody stump and says, "Oh crap, sorry about that."'
		print "It tries to put your hand back on, but you collapse."
		print "The last thing you see is the bear shrug and eat you."
		return 'death'

	elif give_it == "say no":
		print "The b`ear looks shocked. Nobody ever told a bear"
		print "with a broadsword 'no'. It asks, "
		print '"Is it because it\'s not katana? I could go get one"'
		print "It then runs off and now you notice a big iron gate."
		print '"Where the hell did that come from? You say.'

		return 'big_iron_gate'


def big_iron_gate():
	print "You walk upto big iron gate and there's a handle."

	open_it = raw_input(prompt)

	if open_it == "open it":
		print "You open it and you are free!"
		print "There are mountains. And berries! And..."
		print "Oh, but then the bear comes with his katana and stabs you."
		print '"Who\'s laughing now!? Love this katana."'

		return "death"

	else:
		print "That doesn't seem sensible. I mean, the door's right there."
		return 'big_iron_gate'


#This is a dictionary which maps its element names(string values) to pre defined functions(doors)
ROOMS = {
	
	"death": death,
	"princess_lives_here": princess_lives_here,
	"gold_koi_pond": gold_koi_pond, 
	"big_iron_gate": big_iron_gate,
	"bear_with_sword": bear_with_sword 
}

def runner(map, start):
#This statement declares a variable called next and assign it the value of the second argument we've passed
# that is a string and the element name in the dictionary ROOMS
	next = start

#This loop gets the game going by moving through the various doors(pre-defined functions)
	while True:
		#This statement assign variable room the function that is mapped by a string value next
		room = map[next]
		print "\n---------------"
		#This statement runs the room() function we just defined above
		# and assign its return value to the variable next
		# which further through the loop runs the next door. and the process goes on until
		# interpreter encounter exit function which is there in death function 
		next = room()

#This statement execute the function runner(), which takes two arguments, one is ROOMS dictionary
# and other is a string value, that is the element one of the element name of the dict we've passed
runner(ROOMS, "princess_lives_here")

