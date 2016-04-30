"""For letters begining with consonants. Take all consonants before the first vowel and add
them the they end of the word followed by "ay"
e.g banana -> anana-bay
	trash -> ash-tray

For words beginning with vowels, just add yay at the end

eat -> eat-yay

"""

VOWELS = ["A", "E", "I", "O", "U"]

def pig_latin(word):
	if word[0].upper() in VOWELS:
		return word + "-yay"
	else:
		new = word.lstrip("bcdfghjklmnpqrstvwxyz")
		ind = len(word) - len(new)
		return new + "-" + word[0:ind] + "ay"


if __name__ == '__main__':
	print "banana -> " + pig_latin("banana")
	print "trash -> " + pig_latin("trash")
	print "eat -> " + pig_latin("eat")



