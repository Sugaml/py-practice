"""Variable Length Positional Arguments (*args):"""
""" This allows a function to accept any number of positional arguments as a tuple."""

def multiply(*args):
    result = 1
    for num in args:
        result *= num
    return result

print(multiply(2, 3, 4))
 