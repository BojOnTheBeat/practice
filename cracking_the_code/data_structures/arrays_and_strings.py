"""Implementations of the different queestions in the cracking the code interview book
"""


"""1: Implement an algorithm to determine if a string has all unique characters. What if you can't use additional data structures?
"""


"""(str) -> bool
"""
def is_all_unique(string):
	#O(n^2) --- QUite slow because of the count method which takes O(n) time
	
	if len(string) > 256: # If the length of the string 
	# is greater than the max number of ascii characters then we the string can't possibly have all unique characters
		return False
	else:
		for letter in string:
			if string.count(letter) > 1:
				return False
			else:
				return True


"""(str) -> bool
"""
def faster_unique(string):
	# This should be O(n)

	if len(string) > 256: #Assuming the string is ASCII
		return False
	alphabet = [False] * 256
	for char in string:
		if alphabet[ord(char)]:
			return False
		else:
			alphabet[ord(char)] = True
	return True #Only if all characters are unique




"""3: Given two strings, write a method to decide if one is a permutation of the other
"""
"""(str, str) -> bool
"""

# Algorithm is to turn both strings into lists of characters and sort them. Then compare them
# First check if they're the same length. If not return False early.
def is_permutation(string1, string2):
	# This seems terribly slow though

	list1 = []
	list2 = []
	if len(string1) != len(string2):
		return False

	for char in string1:
		list1.append(char)
		list1.sort()

	for char in string2:
		list2.append(char)
		list2.sort()

	if list1 == list2:
		return True
	else:
		return False





# Test by running (Awful I know, will set up proper unit tests later
if __name__ == '__main__':
	#print faster_unique("string")
	#print faster_unique("banana")
	print is_permutation("ban", "nab")
	print is_permutation("noob", "stop")
	print is_permutation("noob", "boob")









