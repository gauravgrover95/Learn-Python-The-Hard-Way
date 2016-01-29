#this line imports argv module from sys library
from sys import argv

#this line store the arguments you just gave in variables called script and filename in string format
script, filename = argv

#this command creates the object of the file in "txt" variable, this object can be later on utilized to call other support methods
#more info is written at the bottom
txt = open(filename)

#this line just prints the name of the file as the declaration that we are going to print your file
print "Here's your file %r:" %(filename)
print ""
#this line reads the file, that means print the content of the file stored in txt variable on console(standard output)
print txt.read()
print ""
txt.close();
#these lines ask user to input the fileName again through console
#purpose is to show programmer that user is not just limited to arguments for opening files
print "I'll also ask you to type it again:"
file_again = raw_input("> ")

#this line opens the file again and give its content to the variable called txt_again
txt_again = open(file_again)

#this line prints the file that has been opened in variable txt_again on console(standard output)
print txt_again.read()
txt_again.close()


#**//*/*/*/*/*/*/*/**/*/*/*/*/*/**/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/**/*/*/*/*/*/*/*

# list of commands I want you to remember: 	

# • close – Closes the file. Like File->Save.. in your editor.
# • read – Reads the contents of the file, you can assign the result to a variable.
# • readline – Reads just one line of a text file.
# • truncate – Empties the file, watch out if you care about the file.
# • write(stuff) – Writes stuff to the file.

#********************************************
#OPEN FUNCTION : this function creates a file object, which would be utilized to call other support methods assosciated with it
#   SYNTAX: file object = open(file_name [, access_mode][, buffering])
#	BIFFERING: if buffering value is 0 then no buffering occurs, but if buffering value is non zero positive then buffering will occurs and if negative then default behaviour is assumed
#******************************************


# read(...)
#  |      read([size]) -> read at most size bytes, returned as a string.
#  |      
#  |      If the size argument is negative or omitted, read until EOF is reached.
#  |      Notice that when in non-blocking mode, less data than what was requested
#  |      may be returned, even if no size parameter was given.
#  |  
