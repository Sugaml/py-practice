import pandas as pd
import numpy as np

data = {'First_Score':[100, 90, np.nan, 95],
'Second_Score': [30, 45, 56, np.nan],
'Third_Score':[np.nan, 40, 80, 98]}

df = pd.DataFrame(data)
df.isna()


df.fillna(0)