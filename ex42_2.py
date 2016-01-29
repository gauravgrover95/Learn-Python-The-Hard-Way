from sys import exit
from random import randint

prompt = "> "

#Didnt understand what object is actually doing just sitting here
#Maybe its a constructor argment, but how that is working i am unsure
class Game(object):
	
	#This is the constructor that initialises the variables for the object
	#and it initialized the variable quips = list of strings as shown
	def __init__(self, start):
		self.quips = [
			"You died. You kinda suck at this.",
			"Your mom would be proud. If she were smarter.",
			"Such a luser.",
			"I have a small puppy that's better at this."
		]


		#This is how we declare as well as initialize variables in classes
		#secondly constructor initialized another variable start = start that was takena s an argument
		# while initializing the object
		self.start = start

	#This is the algorithm that let the game keep moving and it is easyily understandable i suppose
	def play(self):
		next = self.start

		while True:
			print "\n-----------------"

			# getattr just fetches the function and does not execute it.. for its execution you have to apple paranthesis with it
			#There are 3 more similar functions: hasattr, setattr, delattr .. go find sbout them if you are curious
			room = getattr(self, next)
			next = room()

	#This is the death function that is called when the player dies
	def death(self):
		print self.quips[randint(0, len(self.quips) - 1)]
		#Argument of the exit() function is the exit status, which is
		# 0 for success
		# and anything else for failure(That is program had to end without completion)
		# If some non integral value was passed then, it is printed at last and exit status is set to 1 i.e failure
		exit(1)

	def princess_lives_here(self):
		print "You see a beautiful Princess with a shiny crown."
		print "She offers you some cake."

		eat_it = raw_input(prompt)

		if eat_it == "eat it":
			print "You explode like a pinata full of frogs."
			print "The Princess cackles and eats the frogs. Yum!"
			return 'death'

		elif eat_it == "do not eat it":
			print "She throws the cake at you and it cuts off your head."
			print "The last thing you see is her munching on your torso. Yum!"
			return 'death'
		elif eat_it == "make her eat it":
			print "The Princess screams as you cram the cake in her mouth."
			print "Then she smiles and cries and thanks you for saving her."
			print "She points to a tiny door and says, 'The Koi needs cake too.'"
			print "She gives you the very last bit of cake and shoves you in."
			return 'gold_koi_pond'
		else:
			print "The princess looks at you confused and just points at the cake."
			return 'princess_lives_here'


	def gold_koi_pond(self):
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
			return 'bear_with_sword'
		else:
			print "The Koi gets annoyed and wiggles a bit."
			return 'gold_koi_pond'

	def bear_with_sword(self):
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

			return "death"

		elif give_it == "say no":
			print "The bear looks shocked. Nobody ever told a bear"
			print "with a broadsword 'no'. It asks, "
			print '"Is it because it\'s not a katana? I could go get one!"'
			print "It then runs off and now you notice a big iron gate."
			print '"Where the hell did that come from?" You say.'

			return "big_iron_gate"


	def big_iron_gate(self):
		print "You walk up to the big iron gate and see there's a handle."

		if open_it == "open it":
			print "You open it and you are free!"
			print "There are mountains. And berries! And..."
			print "Oh, but then the bear comes with his katana and stabs you."
			print '"Who\'s laughing now!? Love this katana."'

			return "death"

		else:
			print "That doesn't seem sensible. I mean, the door's right there."
			return 'big_iron_gate'

a_game = Game("princess_lives_here")
a_game.play()


# getattr(...)
#     getattr(object, name[, default]) -> value
    
#     Get a named attribute from an object; getattr(x, 'y') is equivalent to x.y.
#     When a default argument is given, it is returned when the attribute doesn't
#     exist; without it, an exception is raised in that case.
