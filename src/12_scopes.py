# Experiment with scopes in Python.
# Good reading: https://www.programiz.com/python-programming/global-local-nonlocal-variables

# When you use a variable in a function, it's local in scope to the function.
x = 12
#? global variable

def changeX():
    #declare function changeX:
    global x
    #global keyword allows us to change the variable inside the function
    x = 99

changeX()

# This prints 12. What do we have to modify in changeX() to get it to print 99?
print(x)


# This nested function has a similar problem.

def outer():
    y = 120
    #initial y = 120

    def inner():
        return y * 0 + 999
        #using scope to access y to use in inner
        #120*0+999 = 999

    inner()

    # This prints 120. What do we have to change in inner() to get it to print
    # 999? Google "python nested function scope".
    print(inner())

outer()