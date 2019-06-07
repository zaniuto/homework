def funkcja_4(x, y=[]):
    y.append(x)
    print(y)


funkcja_4(3, [])
funkcja_4(3, [4, 5, ])
funkcja_4(6)
funkcja_4(7)


def funkcja_5(x, y=None):
    if y is None:
        y = []
    y.append(x)
    print(y)


funkcja_5(3, [])
funkcja_5(3, [4, 5, ])
funkcja_5(6)
funkcja_5(7)
