# 
# Example file for variables
#

# Declare a variable and initialize it
f = "abc"
print(f)

# # re-declaring the variable works
f = 20
print(f)

# # ERROR: variables of different types cannot be combined
#print("this is a string" + f) ERROR: cannot convert is a stringly typed language
print("this is a string and a , " + str(f))


# Global vs. local variables in functions
    ## local scope, f inside the function is different the f outside
def someFunction():
    f = "def"
    print(f)


someFunction()
print(f)


