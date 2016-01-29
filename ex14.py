from sys import argv

script , user_name, password = argv
prompt = '>>> '

#password protected file
#TBN, that any argument we enter is a string and we cannot compare it with the numbers. just remove the quotation from the below statement and you will know what i mean

if password == "12345":

#This is the main program that was ought to be written without any condition
	print "Hi %s, I'm the %s script" %(user_name, script)
	print "I'd like to ask you a few questions."
	print "Do you like me %s?" %(user_name)
	likes = raw_input(prompt)

	print "Where do you live %s?" %(user_name)
	lives = raw_input(prompt)

	print "What kind of computer do you have?"
	computer = raw_input(prompt)

	print """
	Alright, so you said %r about liking me.
	You live in %r. Not sure Where that is.
	And you have a %r computer. Nice.
	""" %(likes, lives, computer)

else:
	print "wrong password"