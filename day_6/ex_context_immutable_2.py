imie = "Ola"


def wypisz_imie(imie):
    print('level 1', imie)
    imie = 'Ewa'
    def wypisz_imie_2():
        print('level 2', imie)
        def wypisz_imie_3():
            global imie
            print('level 3', imie)
            imie = 'Jan'

        wypisz_imie_3()

    wypisz_imie_2()


wypisz_imie("Ala")
print(imie)