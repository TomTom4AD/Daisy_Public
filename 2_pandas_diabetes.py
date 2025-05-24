import pandas as pd
import numpy as np

df = pd.read_csv('C:\\Users\\vdi-student\\Desktop\\diabetes.csv')
print(df)
print(df.head(3).to_string())
print(f'Kształt Danych: {df.shape}')
print(df.describe().T.round(2).to_string()) #pokaż jak się zachowują te pola w pliku
                                            #T - transpond
                                            #round(2) - rounding
print('Ile braków')
print(df.isna().sum())

# tam gdzie zero albo brak wartosci - dac srednia (bez zer)
for col in ['glucose', 'bloodpressure', 'skinthickness', 'insulin', 'bmi', 'diabetespredigreefunction', 'age']:
    df[col] = df[col].replace(0, np.nan)
    mean_ = df[col].mean()
    df[col].replace(np.nan, mean_, inplace=True)

print('\n\n......po czyszczeniu.....\n')
print(df.describe().T.round(2).to_string())
print('Ile braków')
print(df.isna().sum())

df.to_csv('cukrzyca_po_obróbce.csv')