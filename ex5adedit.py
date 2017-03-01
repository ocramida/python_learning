anthony_name = 'Antonio J. DiMarco'
anthony_age = 47 # not a lie
anthony_height = 74 # inches
anthony_weight = 200 # lbs
anthony_eyes = 'Brown'
anthony_teeth = 'White'
anthony_hair = 'Brown'

print "Let's talk about %r." % anthony_name
print "I'm %r inches tall." % anthony_height
print "I'm %r pounds heavy." % anthony_weight
print "Actually I'm not that heavy."
print "I've got %s eyes and %s hair." % (anthony_eyes, anthony_hair)
print "My teeth are usually %s depending on the tea I drink." % anthony_teeth

# this line is tricky, try to get it exactly right
print "If I add %d, %d, and %d I get %d." % (anthony_age, anthony_height, anthony_weight, anthony_age + anthony_height + anthony_weight)
