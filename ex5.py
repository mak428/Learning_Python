name = 'Muki Krishnan'
age = 15 # not a lie
height = 68 # inches
weight = 110 # lbs
eyes = 'Brown'
teeth = 'White'
hair = 'Black'

print "Let's talk about %s." % name
print "He's %d inches tall." % height
print "He's %d pounds heavy." % weight
print "Actually that's not too heavy."
print "He's got %s eyes and %s hair." % (eyes, hair)
print "His teeth are usually %s depending on the cofee." % my_teeth

#this line is tricky, try to get it exactly right
print "If I add %d, %d, and %d I get%d." % (age, height, weight, age + height + weight)

converted_height = height * 2.54
converted_weight = weight * 0.453592

print "He is %d centimeters tall." % converted_weight
print "He is %d kilograms heavy." % converted_height
