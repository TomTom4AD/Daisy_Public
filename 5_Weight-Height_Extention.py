import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.linear_model import LinearRegression

df = pd.read_csv('weight-height_spaces.csv', delimiter=',')
print(df)
print(type(df))

df.Height += 2.54
df.Weight *= 2.2
print(df.head(3)) # pierwsze 3 wiersze