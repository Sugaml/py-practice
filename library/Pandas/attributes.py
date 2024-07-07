import pandas as pd


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
