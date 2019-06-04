a = {1,2,3}
print('set:', a)

b_list = [3,1,2,3,2,3,1]
b = set(b_list)
print(f'lista: {b_list}, zbiór powstały z listy: {b}')

# Dodawanie do setu:
b.add(4)
print(f'b: {b}')
# Przechowywane są tylko unikatowe wartości
b.add(4)
print(f'b: {b}')

# Część wspólna
print(f'b & a: {b & a}')

