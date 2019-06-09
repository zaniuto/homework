def jest_nieparzysta(x):
    if x % 2!= 0:
        return x, True
    z = [x, False]
    return z
y = 2

y1, y2 = jest_nieparzysta(y)
print(y1, y2)

y = jest_nieparzysta(y)
print(y)

print(jest_nieparzysta(3))