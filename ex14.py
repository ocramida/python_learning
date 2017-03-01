# asking Python to use argv dynamic object from sys module
from sys import argv
# arguments script, user_name and age assigned to argv
script, user_name, age = argv
# define variable "prompt" and assign "Give it to me"
prompt = '\"Give it to me!\" '

# print statements using cmd line input via argv arguments.
print "Hi %s I'm the %s script." % (user_name, script)
print "I'd like to ask you a few questions."
print "Do you like me %s?" % (user_name)
# define "likes" variable and using "prompt", i.e. "Give it to me" to prompt raw user input.
likes = raw_input(prompt)

# print statments using cmd line input via argv arguments
print "You're %s." % (age)
print "That's old"
print "Do you still like me?"
# define "not_like" variable and using "prompt", i.e. "Give it to me" to prompt raw user input.
not_like = raw_input(prompt)

# print statement using cmd line input via argv arguments
print "Where do you live %s?" % user_name
# define "lives" variable and using "prompt", i.e. "Give it to me" to prompt raw user input.
lives = raw_input(prompt)
# print statement using cmd line input via argv arguments
print "What kind of computer do you have?"
# define "computer" variable and using "prompt" to prompt raw user input.
computer = raw_input(prompt)

# multiline print statement using output of variables "likes", "not_like", "lives", "computer"
print '''
Alright, so you said \"%s\" about liking me.
You live in \"%s\". Not sure where that is.
I made fun of your age and you said \"%s\" to liking me.
And you have a \"%s\" computer. Nice.
'''  %(likes, lives, not_like, computer)