# grab argument variable module
from sys import argv

# define argv
script, input_file = argv

# define function that reads entire file from argv and prints to screen
def print_all(supplied_file):
	print supplied_file.read()

# define function that goes back to the beginning of file, i.e. byte zero.
def rewind(supplied_file):
	supplied_file.seek(0)
	
# define function to only read one line of a file
def print_a_line(line_count, supplied_file):
	print line_count, supplied_file.readline()

# assign result of opening file (argv argument) into variable "current file"	
current_file = open(input_file)

# print string to alert user of what function we're executing and skip a line
print "First let's print the whole file:\n"

# call "print_all" function defined above
print_all(current_file)

# alert user of what we're doing next
print "Now let's rewind, kind of like a tape."

# calling "rewind" function
rewind(current_file)

# alerting user to what the program is doing next
print "Let's print 3 lines:"

# first defining a new variable and assigning it "1". To enumerate first line as "1"
current_line = 1
# calling function with previously defined variables as arguments 
print_a_line(current_line, current_file)

# redefining variable so the number of the next line to "2".
current_line = current_line + 1
# calling the same "print_a_line" function from above with revised variable/argument 
print_a_line(current_line, current_file)

# redefining variable so the numbering of the third line is incremented by 10.
current_line = current_line + 10
# calling the same "print_a_line" function from above with revised variable/argument 
print_a_line(current_line, current_file)
