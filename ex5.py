name = 'Zed A. Shaw'
age = 35 # not a lie
height = 74 # inches
heightcm = height * 2.54
weight = 180 # pounds
weightkg = weight * 0.45359237
eyes = 'Blue'
teeth = 'White'
hair = 'Brown'

print "Let's talk about %s." % name
print "He's %d inches or %d centimeters tall." % (height, heightcm)
print "He's %d pounds or %d kilograms heavy." % (weight, weightkg)
print "Actually that's not too heavy."
print "He's got %s eyes and %s hair." % (eyes, hair)
print "His teeth are usually %s depending on the coffee." % teeth

# this line is tricky, try to get it exactly right
print "If I add %d, %d, and %d I get %d." % (age, height, weight, age + height + weight)
