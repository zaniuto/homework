x = input("Podaj liczbę: ")
if not x.isdigit():
    x = input("Proszę, podaj liczbę: ")
print(int(x) + 5)