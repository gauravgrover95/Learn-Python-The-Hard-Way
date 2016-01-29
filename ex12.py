age = raw_input("How old are you?")
height = raw_input("How many tall are you?")
weight = raw_input("How much do you weight?")

print "So, you are %r old, %r tall and %r heavy." %(age, height, weight) 

# raw_input(...)
#     raw_input([prompt]) -> string
    
#     Read a string from standard input.  The trailing newline is stripped.
#     If the user hits EOF (Unix: Ctl-D, Windows: Ctl-Z+Return), raise EOFError.
#     On Unix, GNU readline is used if enabled.  The prompt string, if given,
#     is printed without a trailing newline before reading.


# open(...)
#     open(name[, mode[, buffering]]) -> file object
    
#     Open a file using the file() type, returns a file object.  This is the
#     preferred way to open a file.  See file.__doc__ for further information.


