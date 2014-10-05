# Program 3-11
# Michael MacCallum - Python 2.7.5
# Only source used to find code was the official Python 2 documentation https://docs.python.org/2/
#
# This program asks the user to input their name and their age. It then greets them
# and and tells them how old they are.

# Pseudo code in text book explitly stated this variable should be declared globally.
# Declare number variable as string as cheap way to force while loop to execute once,
# without having to add additional conditions on every iteration.
number = ''

def main():
	# Pseudo code in text book explitly stated this variable should be declared globally.
	global number
	# Continue to prompt user for input while the number variable's contents are not all numeric.
	while not str(number).isdigit():
		number = raw_input('Enter a number.\n')

	print showNumber()

def showNumber():
	# Pseudo code in text book explitly stated this variable should be declared globally.
	global number
	# Print feedback string with user entered number concatenated.
	return 'The number you entered is ' + str(number)