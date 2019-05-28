a = 0.1 + 0.1 + 0.1
b = 0.3
# Wynik będzie False, ponieważ float nie jest dokładną reprezentacją ułamków
wynik = a == b
print(wynik)

# Zaokrąglenie liczby można zrealizować funckją round.
# Jest to zaokrąglenie matematyczne.
print(round(45.4563))
liczba_a = round(45.43535, 2)
print(liczba_a)
# Zaokrąglenie przez rzutowanie wyjmuje część całkowitą
print(int(liczba_a))
print(int(2.9))

print(liczba_a % 8)

# Zaokrąglenie może usunąć błędy wynikające z niedokładności flota (zależnie od dokładności zaokrąglenia)
wynik = round(a, 3) == round(b, 3)
print(wynik)
