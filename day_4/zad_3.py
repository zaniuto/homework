liczby = [2, 4324, 25, 43, 4, 5765, 756, 7, 3425, 325, 364]
# znajdz najwiekszy / najmniejszy element w liscie
# napisz program sumujący wszystkie elementy w liscie


suma = 0
_max = flot ('-inf')
_min = float ('inf')
for liczba in liczby:
    suma +=  liczba
    if liczba > _max:
        _max = liczba
    if liczba < _min:
         _min = liczba
print (f'suma liczb {suma}')
print (f'maksymalna liczba {_max}')
print (f'minimalna liczba {_min}')


