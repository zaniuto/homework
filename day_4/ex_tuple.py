a =(1, 0)
print(a)
print(type(a))
# a[1] = 7
# del a[1]
b = 1,
print('b', type(b), b)
c = (1)
print('c', type(c), c)
d = (1,)
print('d', type(d), d)

e = a + (1, 'a')
print('e', type(e), e)
print(f'id a :{id(a)}, e:{id(e)}')

print(f'id a :{id(a)}, copy of a:{id(a[:])}')