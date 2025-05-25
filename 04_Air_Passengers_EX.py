import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

flights = pd.read_csv('C:\\Users\\vdi-student\\Desktop\\Air_Passengers.csv')

# Ewentualna konwersja daty
flights['Date'] = pd.to_datetime(flights['Month'], format='%Y-%m')
flights.set_index('Date', inplace=True)
print(flights.shape)
print(flights.head(5))
print(flights.info())
print("\nStatystyki pasażerów:")
print(flights['#Passengers'].describe())
# 1. Wykres liniowy pasażerów w czasie
plt.plot(flights['#Passengers'])
plt.title('Liczba pasażerów linii lotniczych (1949-1960)')
plt.xlabel('Miesiąc (kolejno)')
plt.ylabel('Liczba pasażerów (tys.)')
plt.show()