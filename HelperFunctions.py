# Determines whether or not the input is a number by attempting to obtain its float value.
# Success indicates the presence of a number, and failure indicates the presence of any
# non-numeric characters.
def isNumber(testValue):
    try:
        float(testValue)
        return True

    except ValueError:
        return False

# Determines whether or not the input string contains a number by iterating over every
# character in the string and checking if it is a digit. The function returns true if 
# any charcter is a digit.
def containsNumber(testValue):
    return any(character.isdigit() for character in testValue)
