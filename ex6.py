x = "there are %d types of people." % 10
binary = "binary"
do_not = "don't"
y = "Those who know %s and those who %s." % (binary, do_not)

print x
print y

print "I said : %r." % x
# embed "x" variable within string
print "I also said :  '%s' ." % y
# embed "y" variable within string

hilarious = False
# define boolean
joke_evaluation = "Isn't that joke so funny?! %r"
# define variable

print joke_evaluation % hilarious
# defined variables to answer question
w = "This is the left side of..."
e = "a string with a right side."
# define variables as strings

print w + e
# print concatenated variables "w" and "e".
# using "+" concatenates strings

