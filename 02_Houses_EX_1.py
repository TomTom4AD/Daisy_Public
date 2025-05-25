import pandas as pd
import numpy as np
from scipy import stats

# Wczytanie danych o cenach domów (Ames Housing data)
df = pd.read_csv('C:\\Users\\vdi-student\\Desktop\\Train_Houses.csv') # plik z danymi treningowymi
print(df.shape)
print(df.head(10))
print(df.info())
# 1. Statystyki opisowe ceny sprzedaży
prices = df['SalePrice']
print("Podstawowe statystyki ceny domu:")
print(prices.describe())
# Dodatkowo obliczamy skośność rozkładu
print("Skośność (skewness) rozkładu cen:", stats.skew(prices))