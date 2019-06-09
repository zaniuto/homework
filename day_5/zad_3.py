# Napisz funkcję prymującą dwa parametry:first_name, last_name
# Zwracającą słownik z kluczami first_name, last_name,
# full_name - imię + nazwisko
# Utrudnienie 1: Jeżeli imię lub nazwisko nie jest podane
#   w wyjściowym słowniku nie ma klucza full_name

def get_full_name(first_name, last_name):
    # return str(first_name) + ' ' + str(last_name)
    # return '{} {}'.format(first_name, last_name)
    return f'{first_name} {last_name}'


def get_name(first_name, last_name):
    slownik = {
        'first_name': first_name,
        'last_name': last_name,
        # 'full_name': get_full_name(first_name, last_name)
    }
    if first_name and last_name:
        slownik['full_name'] = get_full_name(first_name, last_name)
    return slownik

print(get_name('Maciej', 'Kwiatkowski'))
print(get_name('', 'Kwiatkowski'))
print(get_name('Maciej', None))
print(get_name('Maciej', 45))