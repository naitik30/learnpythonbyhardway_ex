def add(a, b):
    print "ADDING %d + %d" % (a, b)
    return a + b

def subtract(a, b):
    print "SUBTRACTING %d - %d" % (a, b)
    return a - b

def multiply(a, b):
    print "MULTIPLYING %d * %d" % (a, b)
    return a * b

def divide(a, b):
    print "DIVIDING %d / %d" % (a, b)
    return a / b


print "Let's do some math with just functions!"

age = add(30, 5)

# ADDING 30 + 5 

height = subtract(78, 4)

# SUBTRACTING 78 - 4

weight = multiply(90, 2)

# MULTIPLYING 90 * 2


iq = divide(100, 2)

# DIVIDING 100 / 2

print "Age: %d, Height: %d, Weight: %d, IQ: %d" % (age, height, weight, iq)

# Age: 35, Height: 74, Weight: 180, IQ: 50

# A puzzle for the extra credit, type it in anyway.
print "Here is a puzzle."

# Here is a puzzle.

what = add(age, subtract(height, multiply(weight, divide(iq, 2))))

print "That becomes: ", what, "Can you do it by hand?"

# That becomes: -4391 Can you do it by hand?

