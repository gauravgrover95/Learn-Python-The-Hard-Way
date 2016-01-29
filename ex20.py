from sys import argv

script, input_file = argv

def print_all(f):
	print f.read()

#This function moves refference cursor 0 bytes ahead from default position 0, reffer bottom for details
def rewind(f):
	f.seek(0)

#This function reads the current line from the cursor(refference position in file) and then move to next line
#Reffer bottom for details
def print_a_line(line_count, f):
	print line_count, f.readline()


#beginning of the main function

current_file = open(input_file)

print "First lets print the whole file:\n"
print_all(current_file)

print "Now lets rewind, kind of like the tape."

rewind(current_file)

print "Lets print 3 lines:"

#These variables doesnt do anything except indicating the line number
#Also they are hard-coded so they are worthless for the real program
current_line = 1
print_a_line(current_line, current_file)

current_line += 1
print_a_line(current_line, current_file)

current_line += 1
print_a_line(current_line, current_file)


#***********************************************************************************************
#when we read file.. it comes to end and for re-reading it, its important to rewind it like a tape, unless it wont read anything, because the reading pointer has come to end

# FILE POSITIONS: 
# 	*tell() method tells you the current position within the file; in other words 
# 	 the next read or write will occur at that many bytes from the beginning of the file

# 	 *seek(offset[, from]) method changes the current position
# 	  offset argument indicates the number of bytes to be moved.
# 	  The from (optional argument, which defaults to 0) argument specifies the refference position from where the bytes are to be moved
# 	  if from = 0, it means beginning of the file 
# 	  if from = 1, it means use the current position
# 	  if from = 2, end of file would be taken as refference

# readline(...)
#  |      readline([size]) -> next line from the file, as a string.
#  |      
#  |      Retain newline.  A non-negative size argument limits the maximum
#  |      number of bytes to return (an incomplete line may be returned then).
#  |      Return an empty string at EOF.
