# PANDAS

## What is Pandas?

Pandas is a Python library used for working with data sets.

It has functions for analyzing, cleaning, exploring, and manipulating data.

The name "Pandas" has a reference to both "Panel Data", and "Python Data Analysis" and was created by Wes McKinney in 2008.

## Why Use Pandas?

Pandas allows us to analyze big data and make conclusions based on statistical theories.

Pandas can clean messy data sets, and make them readable and relevant.

Relevant data is very important in data science.


## What Can Pandas Do?

Pandas gives you answers about the data. Like:

Is there a correlation between two or more columns?
What is average value?
Max value?
Min value?
Pandas are also able to delete rows that are not relevant, or contains wrong values, like empty or NULL values. This is called cleaning the data.

## Installation of Pandas

If you have Python and PIP already installed on a system, then installation of Pandas is very easy.

Install it using this command:

```bash
pip install pandas
```

If this command fails, then use a python distribution that already has Pandas installed like, Anaconda, Spyder etc.

## What is a Series?

A Pandas Series is like a column in a table.

It is a one-dimensional array holding data of any type.


## What is a DataFrame?

A Pandas DataFrame is a 2 dimensional data structure, like a 2 dimensional array, or a table with rows and columns.

## Read CSV Files

A simple way to store big data sets is to use CSV files (comma separated files).

CSV files contains plain text and is a well know format that can be read by everyone including Pandas.

In our examples we will be using a CSV file called 'data.csv'.

## Series

Series is a one-dimensional labeled array capable of holding any data type (integers,
strings, floating point numbers, Python objects, etc.). The values are labeled with
index numbers. First value has index 0, second value has index 1, and so on. These
labels can be used to access a specified value. 

For example,

```bash
import pandas as pd
a = [11, 7, 10]
myvar = pd.Series(a)
print(myvar)
print(myvar[1])
```

# Dataframe Operations

## Head and Tail
To view a small sample of a Series or DataFrame object, use
the head() and tail() methods. The default number of elements to display is five, but
you may pass a custom number.
 
For example,

```bash
print(df.head())
print(df.tail())
```
## Attributes and Underlying Data

Pandas objects have a number of attributes enabling you to access the metadata. The
shape attribute gives the axis dimensions of the object, consistent with ndarray. The
size attribute returns the total number of elements. The index attribute gives index
information and columns attribute gives column information.

For example,

```bash 
data = {
"calories": [420, 380, 390],
"duration": [50, 40, 45]
}
df = pd.DataFrame(data)
print(df)
print(df.shape)
print(df.size)
print(df.index)
print(df.columns)

```


## Working with Missing Data

Missing data can occur when no information is provided for one or more items.
Missing data is a very big problem in a real-life scenario. Missing Data can also refer
to as NA (Not Available) values in pandas. Many datasets simply arrive with missing
data, either because it exists and was not collected or it never existed. In Pandas
missing data is represented by two value: None or NaN.
In order to check missing values in Pandas DataFrame, we use a function isnull()and
notnull(). Both function help in checking whether a value is NaN or not. These
functions can also be used in Pandas Series in order to find null values in a series. We
can also use isna() and notna() functions to check missing values.
 
For example,

```python 
data = {'First_Score':[100, 90, np.nan, 95],
'Second_Score': [30, 45, 56, np.nan],
'Third_Score':[np.nan, 40, 80, 98]}
df = pd.DataFrame(data)
df.isna()
```

In order to fill null values in a datasets, we use fillna(), replace() and interpolate()
function. These functions replace NaN values with some value of their own. The
interpolate() function is basically used to fill NaN values using various interpolation
techniques. 

For example,

```python
data = {'First_Score':[40, 90, np.nan, 95],
'Second_Score': [30, 45, 56, np.nan],
'Third_Score':[np.nan, 40, 80, 98]}
df = pd.DataFrame(data)
df.fillna(0)
```

## Fancy Indexing

Sometimes we need to give a label-based “fancy indexing” to the data frame. The
concept of fancy indexing is simple which means, we have to pass an array of indices
to access multiple array elements at once. This function takes arrays of row and
column labels and returns an array of the values corresponding to each (row, col) pair.

For example,

```python
row = [0, 2]
col = ['Second_Score', 'Third_Score']
print(df.loc[row, col])
```