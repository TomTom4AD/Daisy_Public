
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

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

sns.histplot(df.query('Gender=="Male"').Weight)
plt.show()
sns.histplot(df.query('Gender=="Female"').Weight)
plt.show()