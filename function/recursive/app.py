#  Recursive functions in Python are functions that call themselves directly or indirectly to solve a problem by breaking it down into smaller, similar sub-problems.
#  Recursive functions have two key components: a base case and one or more recursive calls.

def factorial(n):
    if n==0:
        return 1
    else:
        return n*factorial(n-1)

result=factorial(5)
print(result)