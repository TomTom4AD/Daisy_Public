
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.linear_model import LinearRegression

df = pd.read_csv('weight-height_spaces.csv')
print(df)

df.Height *= 2.54
df.Weight /= 2.2
print('Po zmianie jednostek')
print(df.head(10))

#plt.hist(df.Weight)
#plt.show()
#sns.histplot(df.Weight)
#plt.show()

# sns.histplot(df.query('Gender=="Male"').Weight)
# plt.show()
# sns.histplot(df.query('Gender=="Female"').Weight)
# plt.show()

df = pd.get_dummies(df)     #usuwam dane nienumeryczne
print(df)

del df["Gender_Male"]       #usuwam kolumnę Gender_Male bo dane są binarne Female lub Male
print(df)

df = df.rename(columns={"Gender_Female" : "Gender"})      # zamieniam nazwę kolumny Gender_Female na Gender ==> FALSE = Facet, TRUE = KOBIETA

model = LinearRegression()
model.fit(df[['Weight', 'Gender']], df['Weight'])

print(f'Wspolczynnik kierunkowy: {model.coef_}/nWyraz Wolny: {model.intercept_}')

print(f'Weight = Height * {model.coef_[0]} + Gender * {model.coef_[1] + model.intercept_}')