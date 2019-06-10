# Napisz funkcję (z docstringiem) calc, która będzie wykonywała podstawowe
# działania arytmetyczne (dodawanie, odejmowanie, mnożenie, dzielenie).
# Funkcja powinna przyjmować 3 argumetny:
# działanie (jako string), argument 1, argument 2 (domyślnie o wartości 1).
# Wywołaj funkcję na podanej liście parametrów (z użyciem pętli for)

#
# def calc(operator, arg1, arg2):
#     pass
#
#
# test_parameters = [
#     ('+', 2, 2),
#     ('-', 5, 7),
#     ('*', 6, 2.5),
#     ('/', 4),
# ]
#

def _calculate (x, y, z):
    """Funkcja wykonująca podstawowe działania arytmetyczne (dodawanie, odejmowanie, mnożenie, dzielenie).
    Funkcja powinna przyjmować 3 argumetny: działanie (jako string), argument 1, argument 2 (domyślnie o wartości 1)"""


    operation = x
    operations = list('+-*/')
    while operation not in operations:
        operation = input(f"Podaj prawidłowe działanie ({operations}): ")

    var_1 = y
    while isinstance(var_1, str) and not var_1.isdigit():
        var_1 = input("Podaj pierwszą liczbę całkowitą: ")


    var_2 = z
    while isinstance(var_2, str) and not var_2.isdigit():
        var_2 = input("Podaj drugą liczbę całkowitą: ")

    var_1 = int(var_1)
    var_2 = int(var_2)

    result = None
    if operation == '+':
        result = var_1 + var_2
    elif operation == '-':
        result = var_1 - var_2
    elif operation == '*':
        result = var_1 * var_2
    elif operation == '/':
        if var_2 == 0:
            print('Nie można dzielić przez zero!')
        else:
            result = var_1 / var_2

    if result is not None:
        print(f'{var_1} {operation} {var_2} = {result:.2f}')


        def _exit():
            """Funkcja kończąca działanie programu"""
            print( "Koniec" )
            quit()

    # 2 seria danych do przeliczenia w zapętleniu do podania komendy "exit"
    x = input(
        "\n Podaj działania arytmetyczne: \n '+' dodawanie, \n '-' odejmowanie, \n '*' mnożenie, \n  '/'dzielenie)" )
    if x == 'exit':
        _exit()
    y = input( "Podaj pierwszą liczbę całkowitą" )
    if y == 'exit':
        _exit()
    z = input( "Podaj drugą liczbę całkowitą" )
    if z == 'exit':
        _exit()
    _calculate( x, y, z )


# sprawdzenie działania programu
_calculate ('/', 2, 3)



# Utrudnienie 1: Wykorzystaj funkcję calc w kodzie pracy domowej z zajęć 3.
# Utrudnienie 2: Wymuś aby program działał w sposób ciągły - po obliczeniu jednego
# działania pozowlił na wykonanie kolejnego.
# Utrudnienie 3: Spróbuj przekształcić sprawdzanie wejścia
# do programu w funkcję/funkcje, która sprawdza czy nie został podany
# string "exit". Jeżeli tak, przerwij działanie programu.
