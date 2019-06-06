# Napisz program, który będzie wykonywał podstawowe
# działania arytmetyczne (dodawanie, odejmowanie, mnożenie, dzielenie).
# Program będzie prosił o podanie 3 wartości:
# działania (jako string), argument 1, argument 2.


# Utrudnienie 1: Sprawdź czy w przypadku dzielenia dzielnik nie jest 0.
# Utrudnienie 2: Wymuś podanie poprawnych wartości:
# działanie z zakresu: "+", "-", "*","/", argumenty są liczbami całkowitymi
# Podpowiedź: Metoda stringu is digit
# Utrudniene 3: Wypisz tekst w stałej formie - dwa miejsca po przecinku,
# jeżeli jest liczbą z częścią dziesiętną

operations = list('+-*/')
operation = ''
while operation not in operations:
    operation = input(f"Podaj działanie ({operations}): ")

var_1 = ''
while isinstance(var_1, str) and not var_1.isdigit():
    # print('Podano złe wejście')
    var_1 = input("Podaj pierwszą liczbę całkowitą: ")

var_2 = ''
while isinstance(var_2, str) and not var_2.isdigit():
    # print('Podano złe wejście')
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
    # print('Wynik działania', var_1, operation, var_2, '=', result)
