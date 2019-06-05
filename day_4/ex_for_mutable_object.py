a = [1, [1,2], 3, 4]
for elem in a:
    if isinstance(elem, int):
        elem += 3
    else:
        elem.append(3)
    print(elem)
print(a)
print(f'elem {elem}')