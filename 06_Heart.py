import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('heart.csv', comment="#")
print(df)


df = pd.get_dummies(df)     #usuwam dane nienumeryczne