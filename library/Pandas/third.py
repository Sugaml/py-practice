import pandas as pd

calories = {"day1": 420, "day2": 380, "day3": 390}

myvar = pd.Series(calories)

print(myvar)

print("------------------------------------")

myvar1 = pd.Series(calories, index = ["day1", "day2"])

print(myvar1)

print("------------------------------------")

data = {
  "calories": [420, 380, 390],
  "duration": [50, 40, 45]
}

myvar2 = pd.DataFrame(data)

print(myvar2)