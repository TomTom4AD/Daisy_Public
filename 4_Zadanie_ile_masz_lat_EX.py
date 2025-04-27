name = input('Jak masz na imie?')
age = int(input('Ile masz masz lat?'))
salary = int(input('Ile zarabiasz?'))

print('Zobaczmy czy stać Cię na zakupy w Żabce!')

if salary < 3000:
    if age < 18:
        print(f' {name} możesz robić zakupy z mamą!')
    elif age == 18:
        print(f' {name} nie stać Cię na Żabkę, no chyba że z mamą!')
    elif age > 18:
        print(f' {name} może zrobisz jakieś nadgodziny?')
elif salary == 3000:
    if age < 18:
        print(f' {name} możesz robić zakupy z tatą!')
    elif age == 18:
        print(f' {name} nie stać Cię na Żabkę, no chyba że z tatą!')
    elif age > 18:
        print(f' {name} może jednak zrobisz jakieś nadgodziny?')
elif salary > 3000:
    if age < 18:
        print(f' {name} no proszę stać Cię na Żabkę a masz dopiero {age}!')
    elif age == 18:
        print(f' {name} wow, to sobie kup w Żabce coś na pełnioletność!')
    elif age > 18:
        print(f' {name} jest w porządku! Idź do Żabki')