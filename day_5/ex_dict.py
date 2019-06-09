# elementy = { 1:"ola", 0:"ala",  2:"ela" }

# print(elementy)
# print(elementy[1])

slownik = {
    "imie": "Adam",
    "nazwisko":"kowalski",
    "wiek":32 ,
    'imię': "Adam"
}
# print(slownik['imie'])
# print(slownik['imię'])

# slownik['imie'] = 'Maciej'
slownik['adres'] = {
    'kraj': 'Polska',
    'miasto': 'Warszawa'
}
# # Słownik zagnieżdżony
# print(slownik['adres'])
# print(slownik['adres']['kraj'])
#
# klucze
print(slownik.keys())
# wartości
print(slownik.values())

# items() zwraca parę - klucz oraz wartość
for klucz, wartosc in slownik.items():
    print(f"Klucz: {klucz} ma wartość {wartosc}")
#
# if "adres" in slownik.keys():
#     print("Adres dostępny")
# else:
#     print("adres niedostępny")
#
# print(slownik)
# # jeśli przypiszemy wartość do nieistniejącego klucza
# # to zostanie on utworzony
# slownik["miasto"] = "Gdańsk"
# print(slownik)
# # jeśli przypisujemy wartość do istniejącego klucza
# # to zmieniamy/nadpisujemy jego wartość
# slownik["miasto"] = "Gdynia"
# print(slownik)

