# Check if a given word is a palindrome or not
# Returns a boolean

count_
def is_palindrome(word):
	new_word = word.replace(" ", "").replace(",", "").lower()
	if len(new_word) == 1:
		return True
	elif new_word[0] == new_word[-1]:
		return(is_palindrome(new_word[1:-1]))
	else:
		return False


if __name__ == '__main__':
	print is_palindrome("racecar")
	print is_palindrome("paranormal")
	print is_palindrome("acaramanamaraca")
	print is_palindrome("A car, a man, a maraca")




