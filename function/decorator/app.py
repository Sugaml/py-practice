# Decorator functions modify the behavior of other functions without changing their source code.
# They take a function as input, add functionality to it, and return a modified function.
#  Decorators are commonly used for tasks such as logging, authentication, and memoization.

def uppercase_decorator(func):
    def wrapper():
        result=func()
        return result.upper()
    return wrapper

@uppercase_decorator
def greet():
    return "Hello, World!"

print(greet())