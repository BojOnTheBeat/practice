# FizzBuzz test

# Write a program than prints numbers from 1 to 100 and if the number is a multiple of 3, prints "Fizz"
# If the number is a multiple of 5, prints buzz and if the number is a multiple of both, prints fizzbuzz



def fizzbuzz():
	for number in range(101):
		if ((number % 3 == 0) and (number % 5 == 0)):
			print "FizzBuzz"
		elif number % 3 == 0:
			print "Fizz"
		elif number % 5 == 0:
			print "Buzz"
		else:
			print number


if __name__ == '__main__':
	fizzbuzz()


