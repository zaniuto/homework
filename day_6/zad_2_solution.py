# wypisz pary klucz-wartość ze słownika "a"
a = {1: 2, 2: 4, 0: 4}

print('ver 1')
for ii in a.keys():
    print(ii, a[ii])

# # tak nie wolno
# print('ver 1.1')
# for key, val in zip(a.keys(), a.items()):
#     print(ii, a[ii])
# # bo nie mamy pewności że funkcje zwrócą kolekcję
# # w tej samej kolejności

print('ver 2')
for ii in a:
    print(ii, a[ii])


print('ver 3')
for key, val in a.items():
    print(key, val)

