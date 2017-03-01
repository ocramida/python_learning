name = 'Zed A. Shaw'
age = 35 # not a lie
height = 74 # inches
weight = 180 # lbs
eyes = 'Blue'
teeth = 'White'
hair = 'Brown'

print "Let's talk about %s." % name
# printing value contained in "name" variable
print "He's %d inches tall." % height
# printing value contained in "height" variable 
print "He's %d pounds heavy." % weight
# printing value contained in "weight" variable 
print "Actually that's not too heavy."
# printing response express in string 
print "He's got %s eyes and %s hair." % (my_eyes, my_hair)
# printing value contained in "eyes" and "hair" variable 
print "His teeth are usually %s depending on the coffee." % my_teeth
# printing value contained in "teeth" variable 
# this line is tricky, try to get it exactly right
print "If I add %d, %d, and %d I get %d." % (my_age, my_height, my_weight, my_age + my_height + my_weight)
