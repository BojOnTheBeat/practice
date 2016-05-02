# count the number of vowels in the word
VOWELS = "aeiouAeiou"

def count_vowels(word):
	number = 0
	for i in word:
		if i in VOWELS:
			number +=1
	return number


if __name__ == '__main__':
	print count_vowels("paranthesis")
	print count_vowels("Amicable")

