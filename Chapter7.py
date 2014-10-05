# Program 7-1
# Michael MacCallum - Python 2.7.5
# Only source used to find code was the official Python 2 documentation https://docs.python.org/2/
#

# isNumber function can be found in HelperFunction.py in the current directory.
from HelperFunctions import isNumber

def main():
	# Pass strings to the input validation functions, and get hours and payrate back
	hours = validateInput('Enter the number of hours worked')
	payRate = validateInput('Enter the hourly pay rate')
	# Hours and pay rate functions return strings. Convert to floats and multiply.
	grossPay = float(hours) * float(payRate)
	# Pass grossPay to the currency formatter function and stick the return value onto the output string.
	print 'The gross pay is ' + currencyFormat(grossPay)

def validateInput(x):
	output = ''
	# Continuously prompt for valid input until valid input is given.
	while True:
		# Add period and newline character to the input string (user prompt)
		output = raw_input(x + '.\n')
		
		if isNumber(output):
			break
		else:
			print 'Incorrect input, please try again\n'

	return output

def currencyFormat(input):
	# Return a string with commas added appropriately, a dollar sign prepended, 
	# and a format specfier trimming excess digits.
	return "${:,.2f}".format(input)