# Program 6-10
# Michael MacCallum - Python 2.7.5
# Only source used to find code was the official Python 2 documentation https://docs.python.org/2/
#
# This program prompts the user to input the lengths of two sides of a triangle. 
# It then determines the hypotenuse of said triangle with these values.

# isNumber function can be found in HelperFunction.py in the current directory.
from HelperFunctions import isNumber
from math import sqrt

def main():
	# Both a and b are assigned as the return value of the getVariable() function.
	a = getVariable('A')
	b = getVariable('B')
	# Passes a and b to the hypotenuse function to obtain the value of c.
	c = hypotenuse(a, b)

	print 'The length of the hypotenuse is ' + str(c) + '.'

# Function takes a string as input to represent the name of the working side of the
# triangle. It then prompts the user to enter a value for that side. This value is checked
# to make sure it is a number and that it isn't 0 (wouldn't be a triangle) then returned.
def getVariable(side):
	x = 0.0
	while not isNumber(x) or x == 0.0:
		x = raw_input('Enter the length of side ' + side + '.\n')
	return x

# Function takes the length of two sides as input. It then returns the square root
# of the sum of each input squared.
def hypotenuse(a, b):
	return sqrt(float(a) ** 2.0 + float(b) ** 2.0)