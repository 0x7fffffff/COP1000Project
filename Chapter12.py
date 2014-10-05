# Program 12-7
# Michael MacCallum - Python 2.7.5
# Only source used to find code was the official Python 2 documentation https://docs.python.org/2/
#
# This program takes an unformatted phone number as input. It then checks to make sure the input
# is numeric, and 10 digits long. It then formats the phone number to the form (XXX)XXX-XXXX.

# isNumber function can be found in HelperFunction.py in the current directory.
from HelperFunctions import isNumber

def main():
	phoneNumber = ''

	# Prompt the user to enter a phone number while their input is not a number
	while not isNumber(phoneNumber):
		phoneNumber = raw_input('Enter an unformatted 10 digit phone number.\n')

	# Check the length of the input string to make sure it is 10.
	if  len(phoneNumber) == 10:
		# Concatenate formatting characters around slices of string.
		print 'The formatted number is ' + '(' + phoneNumber[0:3] + ')' + phoneNumber[3:6] + '-' + phoneNumber[6:10] +'\n'
	else:
		print 'That number is not 10 digits.\n'