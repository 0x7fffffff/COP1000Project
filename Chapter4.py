# Program 4-7
# Michael MacCallum - Python 2.7.5
# Only source used to find code was the official Python 2 documentation https://docs.python.org/2/
#
# This program takes either an integer or a floating point number as input and outputs
# what the corresponding letter grade would be for the input grade.

# isNumber function can be found in HelperFunction.py in the current directory.
from HelperFunctions import isNumber
from math import floor

def main():
	# Score is initialized as a string for for the while loop to iterate once, without
	# needing to add additional checks on each iteration.
	score = ''
	# Letter grades are added to an array because they will later be accessed by index.
	grades = ['F','D','C','B','A']

	# Continue to prompt user to enter their test score as long as the input is not numeric.
	while not isNumber(score):
		score = raw_input('Enter your test score.\n')
		
		# Letter is initialized to 'F' or grades[0] because the likelyhood of getting an 'F' is 
		# greater than any other grade. This also disgards any potential problems when idx is negative.
		letter = grades[0]

		# Handle indexes 1 and up (Grades 'D' - 'A')
		if score >= 60.0:
			# Get index based on grade
			idx = int(floor((float(score) - 50.0) / 10.0))

			# Make sure that the index is within the array's bounds. Grades 100 and up cause
			# the index to exceed the array's bounds.
			if len(grades) > idx:
				letter = grades[idx]
			# If the grade is 100 or higher, we assume it to be an 'A'
			else:
				letter = grades[len(grades) - 1]

		print 'Your grade is ' + letter + '.'