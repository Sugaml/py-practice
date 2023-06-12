#Higher-order functions are functions in Python that can take other functions as arguments or return functions as results.

def add(x,y):
    return x+y

def subtract(x,y):
    return x-y

def multiply(x,y):
    return x*y

def apply_operation(operation,x,y):
    return operation(x,y)

#Using the higher order function
result1=apply_operation(add,3,4)
print(result1)

result2=apply_operation(subtract,8,6)
print(result2)

result3=apply_operation(multiply,2,6)
print(result3)