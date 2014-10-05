# Program 8-9
# Michael MacCallum - Python 2.7.5
# Only source used to find code was the official Python 2 documentation https://docs.python.org/2/
#
# This program picks randomly between 0 and 1, and uses the result to determine which function 
# it should use to output the sum of integers in an array.

from random import randint as randy

def main():
	# Get random integer from 0 to 1
	i = randy(0,1)
	total = 0

	# Use the random number to determine which way to solve the problem.
	if i == 0:
		total = rightWay()
	else:
		total = longWay()
	
	print 'The sum of the array elements is ' + str(total)

def longWay():
	size = 5
	numbers = [2,4,6,8,10]
	total = 0
	index = 0
	
	# Do the summation manually. Iterate over a range and add the array's value at that
	# index to the total value
	for index in xrange(size):
		total += numbers[index]

	return total

# Utilize standard libraries to accomplish the same task.
def rightWay():
	return sum([2,4,6,8,10])