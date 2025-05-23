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

#sns.histplot(df.query('Gender=="Male"').Weight)     #drukuje wykres "Weight" dla Gender = Male
#sns.histplot(df.query('Gender=="Female"').Weight)   #drukuje wykres "Weight" dla Gender = Female
#plt.show()

#zmiana Gender na dane numeryczne
df = pd.get_dummies(df)
del df['Gender_Male']
df = df.rename(columns={'Gender_Female' : 'Gender'})
print(df.head())
# False = facet, True = kobieta

model = LinearRegression()
model.fit(df[['Height', 'Gender']], df['Weight']) # weź 'Height' i weź 'Gender' i naucz się przez "fit"

# coef_ parametr "a" w funkcji y = ax + b,
# intercept_ to wyraz wolny b
print(f'Wspoczynnik kierunkowy: {model.coef_}\nWyraz wolny: {model.intercept_}')

print(f'Weight = Height * {model.coef_[0]} + Gender * {model.coef_[1]} + {model.intercept_}')
print(model.predict([[160, 1]])) # ile waży pani co ma 160cm wzrostu
