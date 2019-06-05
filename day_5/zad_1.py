# Napisz funkcję wyświetlającą imię i nazwisko,
# obie z wielkiej litery, niezależnie od wejścia


def name(first_name, last_name):
    pass

# wywołując funkcje bez jawnego podania nazw argumentów,
# argumenty przypisywane są w kolejnosci podania ich w nagłowku funkcji
name('Maciej', 'Kwiatkowski')

b = 'Maciej'
name(b, b) # funkcję można wywołać podstawiając za wartość argumentu zmienną
name(first_name='Maciej', last_name='Maciej') # funkcji nie "obchodzi" wartośc zmiennej, może być taka sama
# jeżeli argumenty podawane są jawnie (explicite) mogę być podane w innej kolejności niż nagłówek funkcji
name(last_name='Kwiatkowski', first_name='Maciej')