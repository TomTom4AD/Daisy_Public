imie = input('Jak masz na imie?')
wiek = int(input('Ile masz lat?'))

print('Czy jesteś dorosły?')

if wiek < 18:
    print(f'Siema {imie}, masz {wiek} lat!')
    print(f'Jeszcze Ci brakuje {18-wiek} lat!')
elif wiek >= 18:
    print(f'Siema {imie}, masz {wiek} lat!')
    print(f'Masz już {18+wiek} lat, czyli {wiek} ponad 18 lat!')