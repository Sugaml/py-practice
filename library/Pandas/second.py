import pandas as pd

a = [1, 7, 2]

myvar = pd.Series(a)

print(myvar)


myvar1 = pd.Series(a, index = ["x", "y", "z"])

print(myvar1)