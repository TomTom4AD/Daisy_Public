import pandas as pd

df = pd.read_csv('C:\\Users\\vdi-student\\Desktop\\diabetes.csv')
print(df)
print(df.head(3).to_string())
print(f'Kształt Danych: {df.shape}')
print(df.describe().T.round(2).to_string()) #pokaż jak się zachowują te pola w pliku
                                            #T - transpond
                                            #round(2) - rounding
