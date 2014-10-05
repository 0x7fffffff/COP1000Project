# Program 2-4
# Michael MacCallum - Python 2.7.5
# Only source used to find code was the official Python 2 documentation https://docs.python.org/2/
#
# This program asks the user to input their name and their age. It then greets them
# and and tells them how old they are.

# containsNumber function can be found in HelperFunction.py in the current directory.
from HelperFunctions import containsNumber

def main():
	name = 0
	age = 0
		
	# Continue to prompt user for name input if contains numeric characters
	while containsNumber(str(name)):
		name = raw_input('Enter your name.\n')

	# Continue to prompt user for age if input is not a digit, or if the 
	# digit's value is less than or equal to zero or greater than 135.
	# Oldest living human is currently 116, so this should be an alright limit.
	while not str(age).isdigit() or int(age) <= 0 or int(age) > 135:
		age = raw_input('Enter your age.\n')

	print 'Hello ' + name
	print 'You are ' + age + ' years old.'