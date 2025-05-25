import pandas as pd
import numpy as np
from scipy import stats
import matplotlib.pyplot as plt

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

# Statystyki opisowe ceny sprzedaży
import seaborn as sns

prices = df['SalePrice']
desc = prices.describe()
skewness = stats.skew(prices)

# Wykres rozkładu cen domów
plt.figure(figsize=(10, 6))
sns.histplot(prices, kde=True, bins=30, color='skyblue')
plt.title(f'Rozkład cen domów\nSkośność: {skewness:.2f}')
plt.xlabel('Cena sprzedaży')
plt.ylabel('Liczba domów')
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.show()

# 2. Wykrywanie wartości odstających dla ceny (SalePrice)

# a) Zastosowanie reguły z-score: uznajemy obserwacje z |z|>3 za outlier

z_scores = np.abs(stats.zscore(prices))
outlier_idx = np.where(z_scores > 3)[0]
print("\nLiczba obserwacji odstających wg z-score > 3:", len(outlier_idx))
print("Indeksy obserwacji odstających:", outlier_idx)

# Wyświetlenie kilku ekstremalnych cen wraz z powierzchnią dla tych obserwacji

print("\nOutliery - ceny i powierzchnia:")

for idx in outlier_idx:
    print(f"Index {idx}: Price={df.at[idx, 'SalePrice']}, GrLivArea={df.at[idx, 'GrLivArea']}")

# b) Wykres pudełkowy ceny sprzedaży

import matplotlib.pyplot as plt
plt.boxplot(prices, vert=False)

plt.title('Wykres pudełkowy - SalePrice')
plt.show()# 2. Wykrywanie wartości odstających dla ceny (SalePrice)

# a) Zastosowanie reguły z-score: uznajemy obserwacje z |z|>3 za outlier

z_scores = np.abs(stats.zscore(prices))
outlier_idx = np.where(z_scores > 3)[0]

print("\nLiczba obserwacji odstających wg z-score > 3:", len(outlier_idx))
print("Indeksy obserwacji odstających:", outlier_idx)

# 3. Zależność ceny od powierzchni mieszkalnej (GrLivArea)
plt.scatter(df['GrLivArea'], df['SalePrice'], alpha=0.5)
plt.title('Cena vs. Powierzchnia mieszkalna')
plt.xlabel('GrLivArea (sq ft)')
plt.ylabel('SalePrice ($)')
plt.show()
# 4. Korelacja Pearsona między wybranymi cechami a ceną
features = ['GrLivArea', 'OverallQual', 'TotalBsmtSF', 'YearBuilt']
for feat in features:
    # This line needs to be indented as it's part of the for loop block
    r, pval = stats.pearsonr(df[feat], df['SalePrice'])
    # This line also needs to be indented and fixed for proper string formatting
    print(f"Korelacja Pearsona: SalePrice vs {feat}: r = {r:.2f}, p-value = {pval:.1e}")
