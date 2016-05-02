# Check if a given word is a palindrome or not
# Returns a boolean

# TODO: Take car of punctuation and space cases...i.e perfome some sort of strip()

def is_palindrome(word):
	if len(word) == 1:
		return True
	elif word[0] == word[-1]:
		return(is_palindrome(word[1:-1]))
	else:
		return False


if __name__ == '__main__':
	print is_palindrome("racecar")
	print is_palindrome("paranormal")
	print is_palindrome("acaramanamaraca")



