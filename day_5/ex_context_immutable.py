imie = "Ola"


def wypisz_imie(imie):
    print(imie)

print('-'*15)
print('Wersja 1')
print(imie)
wypisz_imie("Ala")
print(imie)


def wypisz_imie_2():
    duze_imie = imie.upper()
    return duze_imie

print('-'*15)
print('Wersja 2')
print(wypisz_imie_2())
print(imie)


def wypisz_imie_3():
    global imie
    imie = imie.upper()
    return imie


print('-'*15)
print('Wersja 3')
print(wypisz_imie_3())
print(imie)


# imie = "Ola"
# # Błędna wersja
# def wypisz_imie_4():
#     imie = imie.upper()
#     return imie
#
# print('-'*15)
# print('Wersja 4')
# print(wypisz_imie_4())
# print(imie)