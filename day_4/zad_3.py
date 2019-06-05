liczby = [2, 4324, 25, 43, 4, 5765, 756, 7, 3425, 325, 364, -3]
# znajdz najwiekszy / najmniejszy element w liscie
# napisz program sumujący wszystkie elementy w liscie

suma = 0
_max = float('-inf')
_min = float('inf')
for liczba in liczby:
    # suma = suma + liczba
    suma += liczba
for liczba in liczby:
    if liczba > _max:
        _max = liczba
for liczba in liczby:
    if liczba < _min:
        _min = liczba
print(f'suma liczb {suma}')
print(f'maksymalna liczba {_max}')
print(f'minimalna liczba {_min}')
print(f'suma: {sum(liczby)}, max: {max(liczby)}, min: {min(liczby)}')
