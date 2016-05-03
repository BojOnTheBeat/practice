def count_words(word):
	count = 0
	count = len(word.split())
	return count


if __name__ == '__main__':
	print count_words("Boj is dope")
