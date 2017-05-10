# -*- coding: utf-8 -*-

my_name = 'Zed A. Shaw'
my_age = 35 # not a lie
my_height = 74 # inches
my_weight = 180 # lbs
my_eyes = 'Blue'
my_teeth = 'White'
my_hair = 'Brown'


print "Let's talk about %s." % my_name

#let's talk about Zed A. Shaw

print "He's %d inches tall." % my_height

# He's 74 inches tall.

print "He's %d pounds heavy." % my_weight

# He's 180 pounds heavy.

print "Actually that's not too heavy."

#Actually that's not too heavy.

print "He's got %s eyes and %s hair." % (my_eyes, my_hair)

#He's got Blue eyes and Brown hair.

print "His teeth are usually %s depending on the coffee." % my_teeth

#His teeth are usually White depending on the coffee. 

# this line is tricky, try to get it exactly right
print "If I add %d, %d, and %d I get %d." % (
    my_age, my_height, my_weight, my_age + my_height + my_weight)

# If I add 35, 74, and 180 I get 289

