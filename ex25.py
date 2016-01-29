#This file contains all the modified functions to work on strings
#here is some more text
#and i am writing here like crazy

#split function return multiple strings seperated by the seperator(in this case, white space)
#for more details see below.
def break_words(stuff):
	"""This function will break up words for us."""
	words = stuff.split(" ")
	return words

#sort function: returns the new sorted list of words which were passed as an argument
#for more information check below
def sort_words(words):
	"""Sorts the words."""
	return sorted(words)

#pop function is applied on a list
# It removes and returns  the item at given index which by default is last(position in list like arrays(starting from 0))
#for more information on pop and index error see below
def print_first_word(words):
	"""Prints the first word after popping it off."""
	word = words.pop(0)
	print word

#negative arument of the pop gives position of the element in list from last element
#example -1: last word, -2: second last word -3: thord last word.... and so on
def print_last_word(words):
	"""Prints the last word after popping it off."""
	word = words.pop(-1)
	print word

def sort_sentence(sentence):
	"""Takes in a full sentence and returns the sorted words."""
	words = break_words(sentence)
	return sort_words(words)

def print_first_and_last(sentence):
	"""Prints the first and last words of the sentence."""
	words = break_words(sentence)
	print_first_word(words)
	print_last_word(words)

def print_first_and_last_sorted(sentence):
	"""Sorts the words then prints the first and last one."""
	words = sort_sentence(sentence)
	print_first_word(words)
	print_last_word(words)

#************/*/*/****************/*/*/*****************/*/*/******************/*/***********

# sorted(...)
#     sorted(iterable, cmp=None, key=None, reverse=False) --> new sorted list
# (END)


 # split(s, sep=None, maxsplit=-1)
 #        split(s [,sep [,maxsplit]]) -> list of strings
        
 #        Return a list of the words in the string s, using sep as the
 #        delimiter string.  If maxsplit is given, splits at no more than
 #        maxsplit places (resulting in at most maxsplit+1 words).  If sep
 #        is not specified or is None, any whitespace string is a separator.

 # pop(...)
 # |      L.pop([index]) -> item -- remove and return item at index (default last).
 # |      Raises IndexError if list is empty or index is out of range.
