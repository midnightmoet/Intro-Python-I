"""
Python provides a number of ways to perform printing. Research
how to print using the printf operator, the `format` string
method, and by using f-strings.
"""
# Using the printf operator (%), print the following feeding in the values of x,
# y, and z:
# x is 10, y is 2.25, z is "I like turtles!"

x = 10
y = 2.24552
z = "I like turtles!"
a = "My name is Nisa"

#string formatting syntax borrowed from C ~~ fun fact
#Allows us to insert a string. the %s token is replaced by whatever we want to pass into the string
# print("blah blah %s" % x)

print("x is %s" % x)
print("y is %s" % y)
print("z is %s" % z)

# Use the 'format' string method to print the same thing

####My funny example###
my_string = "Look ma, {} can do teh {} {}!"
print(my_string.format("I", "Python", "thinggy"))

#New Method preferred
print("x is {}".format(x))
print("y is {}".format(y))
print("z is {}".format(z))

print("Look ma: {}".format(a))


# Finally, print the same thing using an f-string
print(F"x is {x}")
print(F"y is {y}")
print(F"z is {z}")

###My example
print(F"Lookie:  {a} oh noes!")