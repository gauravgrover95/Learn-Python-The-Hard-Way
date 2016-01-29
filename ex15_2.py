
print "I'll ask you to type the file name here:"
file_again = raw_input("> ")
txt_again = open(file_again)
print txt_again.read()