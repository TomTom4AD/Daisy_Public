
import pandas as pd

df = pd.read_csv('weight-height.csv', delimiter = ';')
print(df)

df.Height *= 2.54
df.Weight /= 2.2
print('Po zmianie jednostek')
print(df.head(10))