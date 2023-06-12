#   Lambda functions are small, anonymous functions that can be defined in a single line using the lambda keyword.
#   They are commonly used for simple, one-time operations without the need for a named function.

#Reular named function
def square(x):
    return x**2

print(square(5)) 

#Equivalent lamda function
square_lambda =lambda x:x**2

print(square_lambda(10))

#Lamda function for adding two numbers
add_lambda=lambda x,y:x+y

print(add_lambda(3,5))