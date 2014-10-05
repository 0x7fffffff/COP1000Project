# Michael MacCallum - Python 2.7.5
# Only source used to find code was the official Python 2 documentation https://docs.python.org/2/
#
# This program shows the user what other programs it is capable of executing, asks the user to
# specify the number of the chapter corresponding to the program to be run. It then runs the
# selected program. A majority of this program runs within a loop, and is capable of running
# as many programs as desired sequentially as long as the user wishes to continue.

# Not the most Pythonic thing to do, but it's a lot of importing to break onto multiple lines.
import Chapter2, Chapter3, Chapter4, Chapter5, Chapter6, Chapter7, Chapter8, Chapter10, Chapter12, Chapter14

# Create dictionary containing keys for the available chapter numbers, and set their values
# to the corresponding modules that contain their individual programs.
dict = {
    '2':Chapter2,
    '3':Chapter3, 
    '4':Chapter4, 
    '5':Chapter5, 
    '6':Chapter6, 
    '7':Chapter7, 
    '8':Chapter8, 
    '10':Chapter10, 
    '12':Chapter12, 
    '14':Chapter14,
}


# Executes the main() function located in the module that corresponds to the input chapter number.
def runModuleForChapter(chapter):
    return dict[chapter].main()



# Enumerates all the keys in the dictionary to show the user the available chapter numbers
print '\n\nHello! I can execute programs one at a time from chapters:', [int(x) for x in dict.keys()]

# Gives the ability to continue to execute more programs without restarting the Main.py process.
while True:
    print '\nPlease enter the chapter number of the program you\'d like to execute.'

    # Initialized as a string to force the while loop to iterate at least once, without the need
    # of additional checks on each iteration.
    selectedChapter = ''

    # Continuously prompts the user to enter a chapter number while the input is not a key in the dictionary.
    while not selectedChapter in dict:
        selectedChapter = raw_input('Enter a chapter number.\n')

    # Run the desired program.
    print 'Executing module', selectedChapter,'\n'
    runModuleForChapter(str(selectedChapter))

    continueInput = ''
    # Prompt the user to determine whether or not they want to continue executing programs. If they
    # Don't, break the main while loop.
    while continueInput.lower() not in {'y', 'n', 'yes', 'no'}:
        continueInput = raw_input('\n\nWould you like to run another program? (y/n)\n')

    if continueInput in {'n', 'no'}:
        print 'Goodbye!'
        break

