import pandas as pd
from scipy.stats import skew, kurtosis
import matplotlib.pyplot as plt
import seaborn as sns

# Wczytujemy dane z pliku CSV (plik 'train.csv' powinien być w bieżącym katalogu)
df = pd.read_csv('C:\\Users\\vdi-student\\Desktop\\Train_Titanic.csv')  # zakładamy, że nazwa pliku to titanic_train.csv

# 1. Podstawowe informacje o zbiorze
print("Liczba wierszy i kolumn:", df.shape)  # rozmiar danych
print(df.columns)  # nazwy kolumn
print(df.head(5))  # podgląd pierwszych 5 rekordów
# Sprawdzenie braków danych w poszczególnych kolumnach
print("\nBrakidanych w kolumnach:")
print(df.isnull().sum())  # liczba braków (NaN) w każdej kolumnie

# 2. Statystyki opisowe dla zmiennych numerycznych
print("\nStatystykiopisowe zmiennych numerycznych:")
print(df.describe())

# Sprawdźmy dane numeryczne
num_cols = df.select_dtypes(include='number').columns
print("Kolumny numeryczne:", list(num_cols))

# Miary położenia i rozproszenia
print("\n Statystyki opisowe:")
print(df[num_cols].describe())

# Miary położenia i kształtu dla kolumny 'Age'
age = df['Age'].dropna()

print(f"\n Średnia wieku: {age.mean():.2f}")
print(f"Medianawieku: {age.median():.2f}")
print(f"Kwartyl1 (Q1): {age.quantile(0.25):.2f}")
print(f"Kwartyl3 (Q3): {age.quantile(0.75):.2f}")
print(f"Rozstępmiędzykwartylowy(IQR): {age.quantile(0.75) - age.quantile(0.25):.2f}")

# Miary kształtu
print(f'\n Skośność (skewness): {skew(age):.2f}')
print(f'Kurtoza(kurtosis): {kurtosis(age):.2f}')

# Histogram wieku z gęstością
plt.figure(figsize=(8, 4))
sns.histplot(age,kde=True,bins=30,color='skyblue')
plt.title("Rozkład wieku pasażerów")
plt.xlabel("Wiek")
plt.ylabel("Liczba pasażerów")
plt.axvline(age.mean(),color='red',linestyle='--',label='Średnia')
plt.axvline(age.median(),color='green',linestyle='--',label='Mediana')
plt.legend()
plt.tight_layout()
plt.show()

# 3. Analiza przeżywalności w grupach kategorycznych
# Tabela częstości: płeć vs przeżycie
survival_by_sex= pd.crosstab(df['Sex'],df['Survived'])
print("\nPrzeżycie względem płci:")
print(survival_by_sex)
# Obliczenie procentu przeżycia dla płci
survival_rate_by_sex= survival_by_sex.div(survival_by_sex.sum(axis=1),axis=0) * 100
print("\n% przeżycia wg płci:")
print(survival_rate_by_sex)
# Tabela częstości: klasa vs przeżycie
survival_by_class= pd.crosstab(df['Pclass'],df['Survived'])
print("\nPrzeżycie względem klasy kabiny:")
print(survival_by_class)
# % przeżycia dla każdej klasy
survival_rate_by_class= survival_by_class.div(survival_by_class.sum(axis=1),axis=0) * 100
print("\n% przeżycia wg klasy:")
print(survival_rate_by_class)

# Wiek pasażerów wg płci (z punktami)
plt.figure(figsize=(12, 6))
sns.boxplot(x='Sex', y='Age', data=df)
plt.title('Wiek pasażerów wg płci (z punktami)')

plt.xlabel('Płeć')
plt.ylabel('Wiek')
plt.grid(True, alpha=0.3)
plt.show()