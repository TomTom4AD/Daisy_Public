# import pandas as pd

# df = pd.read_csv('C:\\Users\\vdi-student\\Desktop\\Train_Titanic.csv')
# print(df.head)
# print(df.info)
# print(df)
#print(df.head(3).to_string())

import pandas as pd

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
