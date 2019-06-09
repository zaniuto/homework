a = {1: 3, 2: 5, 4: 7}

# czy wartość 7 znajduje się w słowniku "a"?

print('ver 1')
print(7 in a.values())

print('ver 2')
def check(a, var):
    for ii in a:
        if a[ii] == var:
            return True
    return False
print(check(a, 7))