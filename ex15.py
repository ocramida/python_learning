# asking python to use argv dynamic object from sys module
from sys import argv

# assigning arguments to argv to hold. Arguments are passed to the program at runtime.
script, filename = argv

# define "txt" variable to hold returned value from running open cmd on file object "filename". 
txt = open(filename)

# print string with content of file object "filename". User sees name of file on-screen
print "Here's your file %r:" % filename

# print content of .txt to screen. User see contents of file on-screen. 
print txt.read()

# prompt user to input filename
print "Type the filename again:"

# define new variable "file_again" to contain user input. User inputs filename again.
file_again = raw_input("> ")

# define new variable "txt_again" to returned value of open(file_object). File assigned to "fileagain" is open 
txt_again = open(file_again)

# print result of reading txt_again, which is result of open (file_object). User sees file content on-screen.
print txt_again.read()

