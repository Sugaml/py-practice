import pandas as pd


df1 = pd.DataFrame({"Common": ["A", "B", "C", "D", "E"],
"Name": ["John", "Alice", "Emma", "Watson", "Harry"],
"Age": [18, 19, 20, 21, 15]})

df2 = pd.DataFrame({"Common": ["A", "B", "C", "D", "E"],
"Sport": ["Cricket", "Football", "Table Tennis", "Badminton", "Chess"],
"Movie": ["Jumanji", "Black Widow", "End Game", "Mr. Robot",
"Matrix"]})

df3 = pd.merge(df1, df2, how = "left", on = "Common")
print(df3)