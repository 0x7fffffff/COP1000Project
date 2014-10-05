# Program 14-1
# Michael MacCallum - Python 2.7.5
# Only source used to find code was the official Python 2 documentation https://docs.python.org/2/
#
# This program creates a class with three properties. It then assigns values to these
# three properties, and then reads their values back out.

# Create the CellPhone class
class CellPhone(object):
	# Initialize the class
	def __init__(self):
		super(CellPhone, self).__init__()
		# Assign empty strings to all the properties
		self.manufacturer = ''
		self.modelNumber = ''
		self.retailPrice = ''

	# Define the setters.
	def setManufacturer(self, x):
		self.manufacturer = x

	def setModelNumber(self, x):
		self.modelNumber = x

	def setRetailPrice(self, x):
		self.retailPrice = x

	# Define the getters.
	def getManufacturer(self):
		return self.manufacturer

	def getModelNumber(self):
		return self.modelNumber

	def getRetailPrice(self):
		return self.retailPrice

def main():
	# Create an instance of the CellPhone class
	myPhone = CellPhone()

	# Assign values to the cell phone instance's properties.
	myPhone.setManufacturer('Motorola')
	myPhone.setModelNumber('M1000')
	myPhone.setRetailPrice('199.99')

	# Use the cell phone class' getters to print the values of the properties.
	print 'The manufacturer is ' + myPhone.getManufacturer()
	print 'The model number is ' + myPhone.getModelNumber()
	print 'The retail price is ' + myPhone.getRetailPrice()