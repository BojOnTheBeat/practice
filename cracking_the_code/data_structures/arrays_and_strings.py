"""Implementations of the different queestions in the cracking the code interview book
"""

"""1: Implement an algorithm to determine if a string has all unique characters. What if you can't use additional data structures?
"""


"""(str)->bool
"""
def is_all_unique(string):
	#flag = False
	if len(string) > 256: # If the length of the string 
	# is greater than the max number of ascii characters then we the string can't possibly have all unique characters
		return False
	else:
		for letter in string:
			if string.count(letter) > 1:
				return False
			else:
				return True


if __name__ == '__main__':
	print is_all_unique("string")
	print is_all_unique("banana")