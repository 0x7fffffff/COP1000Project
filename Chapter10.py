# Problem 10-6
# Michael MacCallum - Python 2.7.5
# Only source used to find code was the official Python 2 documentation https://docs.python.org/2/
#
# This program opens a file named 'videoTimes.dat' in the current directory. It then iterates over
# the lines in this file, and sums their float values.

def main():
	INPUT_FILE_NAME = 'videoTimes.dat'
	total = 0.0

	# Open the 'videoTimes.dat' file in read mode, and assign it to the file variable
	file = open(INPUT_FILE_NAME,'r')

	print 'Here are the running times, in seconds, of each video in the project:'
	
	# Continuously read the next line from the file.
	while 1:
		line = file.readline()
		if line:
		# If the line exists, increment the total time variable by the number on this line.
			total += float(line)
			print line.rstrip('\n')
		# Stop iteration when there aren't any more lines.
		else:
			break

	# Close the file.
	file.close()
	
	print 'The total running time of the videos is ' + str(total) + ' seconds.'
