# importing argv dynamic object from sys library/package
from sys import argv

# assigning script and filename -passed to script- arguments/parameter to argv "you define parameters, you make arguments"
script, filename = argv

# passing filename argument/parameter to print function/command/method  
print "We're going to append %r." % filename

# print function/command/method outputting text which is directing the user to a certain "if" action.
print "If you don't want that, hit CTRL-C (^C)."

# print function outputting text which is directing the user to a certain "or" action.
print "If you do want that, hit RETURN."

# use raw_input function to prompt user for input. Prompt is "?"
raw_input("get ready...GO!")

# using print funciton to send notification to user that file will be open
print "Opening the file..."

# defining target object/variable and assigning it to result of opening the filename contained in argv
append = open(filename, 'a')

# calling print function to alert user that open file will be truncated (i.e. contents will be erased)
# print "Truncate the file. Goodbye!"

# calling truncate function/command/method on target object
# looser.truncate() # object/variable.function/method

# print function requesting input from user
print "Now I'm going to ask you for three more lines."

# defining variables/objects and prompting user with string in () 
first_sentence = raw_input("new sentence: ")
second_sentence = raw_input("additonal sentence: ")
third_sentence = raw_input("next sentence: ")

# Passing string to print function
print "I'm going to write these to the file."

# calling write function on target object. Inserting raw_input from above, into file.
append.write(first_sentence) # object.function(argument)
append.write("\n")
append.write(second_sentence)
append.write("\n")
append.write(third_sentence)
append.write("\n")

# letting user know we will be closing the file via print function
print "And finally we close it."

# calling close function on "target" object
append.close()
