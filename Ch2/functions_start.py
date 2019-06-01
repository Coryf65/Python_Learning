#
# Example file for working with functions
#

# define a basic function,
    #the scope is from the start of the ':' and everything in indents
def func1():
    print("I am function 1!")

# function that takes arguments
def func2(arg1, arg2):
    print(arg1, " ", arg2)

# function that returns a value
def cube(x):
  return x*x*x

# function with default value for an argument
# and loop
def power(num, x=1):
    result = 1
    for i in range(x):
        result = result * num
    return result


#function with variable number of arguments
# we loop through every arg and add them all together
# no matter how many ? huh
# you can add normal args but the vaariable arg must be the last in the funtion declaration
def multi_add(*args):
    result = 0
    for x in args:
        result = result + x
    return result


# displaying 

# function does not return a value, we are printing the value of the definition itself
#print(funct1())
print("calling func1()")
func1()
print("printing func1")
print(func1)

print("calling func2(10, 20)")
func2(10, 20)

print("printing func2()")
print(func2(10,20))

print("printing cube(3)")
print(cube(3))

print("printing power(2)")
print(power(2))

print("printing power(2,3)")
print(power(2, 3))

# Python is weird, reversing the order of args. if you supply the names with the
# values then the python interprater can match to the function
print("printing power(x=3, num=2)")
print(power(x=3, num=2))

print("printing multi_add(as many nums as you want !!)")
print(multi_add(10,20,55,6,54,4,8,9,10))
