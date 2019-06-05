litery = ['a', 'b', 'c']


def dodaj_litere(litery, nowa_litera):
    litery.append(nowa_litera)

print('-'*15)
print('Wersja 1')
print(litery)
dodaj_litere(litery, 'a')
print(litery)

litery = ['a', 'b', 'c']


def dodaj_litere(litery, nowa_litera):
    return litery +[nowa_litera]

print('-'*15)
print('Wersja 2')
print(litery)
print(dodaj_litere(litery, 'a'))
print(litery)