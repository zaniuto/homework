# Napisz funkcję podnoszącą podaną wartość (number) do podanej potęgi (index)
# Jeżeli potęga nie jest podana, podnieś do 2. potęgi

def my_pow(number, index=2.):
    """Zwraca liczbę number podniesioną do potęgi index."""
    return number ** index

# Funkcja działa poprawnie tylko dla dodatnich wykładników całkowitych
# def my_pow(number, index=2):
#     mul = 1
#     for ii in range(index):
#         mul *= number
#     return mul

print(my_pow(4, 3))   ## wynik: 64
print(my_pow(2))    ## wynik: 4
print(my_pow(4, 0.5))
