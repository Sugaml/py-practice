import pandas as pd

df = pd.read_csv('data.csv')

print(df.head(10))

# print(df.head()) # Default 5

# The DataFrames object has a method called info(), that gives you more information about the data set.

print(df.info()) 
