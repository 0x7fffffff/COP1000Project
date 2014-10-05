# Program 5-9
# Michael MacCallum - Python 2.7.5
# Only source used to find code was the official Python 2 documentation https://docs.python.org/2/
#
# This program outputs the numbers 1 through 10 and their squares, each in their own column.

def main():
	# Constant 10 as max number
	MAX = 10

	print 'Number\tSquare'
	print '--------------'

	# Iterates from first value to last value. Added 1 for inclusion.
	for x in xrange(1, MAX + 1):
		# Prints string from the concatenation of the current number, a tab character, and
		# the number's square.
		print str(x) + '\t' + str(x ** 2)