# Wyświetl wszystkie elementy listy i jej indeksy
zz = [1,7,3,4,5]

# ii = 0
# # while ii < len(zz):
# for number in zz:
#     print(ii, number)
#     ii += 1

# for ii, number in enumerate(zz):
#     print(ii, number)

for elem in enumerate(zz, start=99):
    print(elem, type(elem))


