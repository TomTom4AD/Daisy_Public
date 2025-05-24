# przyjmie nazwe pliku (zabezpieczenia)
# @przyjmie rozszerzenie
# powie czy rozszerzenie dozwolone - jesli nie to podaj inne
# program napisze ladnie nazwe z rozszerzeniem
from win32pdh import counter_status_error

# program wykona to dla X plikow danych razem

extentions = ['txt', 'csv', 'jpg', 'mp3']

file_name = input('Podaj nazwe pliku:   ')
print(f'Podana nazwa {file_name} \na 2+2 to {2+2}')
# len(x)

counter_a = 0

while True:
    ext_name = input(f'Podaj rozszerzenie:   ')
    if ext_name in extentions:
        print(f'zaakceptowano {ext_name}')
        break
    else:
        print('niepoprawne rozszerzenie')
        counter_a = counter_a + 1   # counter_a += 1 to to samo
        if counter_a == 3:
            break
