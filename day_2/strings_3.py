# Isntieje również "f-string", czyli "formated-string"
# Jest to string, do którego w miejsce oznaczone "{<nazwa-zmiennej>} (<nazwa-zmiennej> to jakaś zmienna)
# wstawiana jest wartość tej zmiennej. Zmienna musi być wcześniej zdefiniowana
a = 0.1 + 0.1 + 0.1
b = 0.3
print(f"a = {a} , b = {b}")

# Możliwe jest także wywołanie metody "format" stringa, która pozwala na zdefiniowanie zmiennych,
# ALE TYLKO NA POTRZEBY FORMATOWANIA stringa, nie nadpisując zmiennych
print("a = {a} , b = {b}".format(a=a, b=b))
print("a = {a} , b = {b}".format(b=a, a=b))
print("a = {b} , b = {a}".format(b=a, a=b))
# Jeżeli miejsca w stringu są nie nazwane, obowiązuje kolejność podania zmiennych
print("a = {} , b = {}".format(a, b))

