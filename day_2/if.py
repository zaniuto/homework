x = input("Podaj liczbę: ")
x = int(x)
if x % 2 == 0:
    print("Podana liczba jest podzielna przez 2!")
    if x % 3 == 0:
        print("Liczba jest pdzielna przez 6")
    elif x > 5:
        print("Liczba większa od 5")
else:
    print("Liczba nieparzysta")
