def divide(a,b):
    if b==0:
        raise ValueError("cannot divide by zero")
    return a/b

try:
    divide(10,0)
except ValueError as e:
    print(e)