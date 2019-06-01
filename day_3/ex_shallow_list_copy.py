aa = [None, [5, 6], 'a', 45, 45]
bb = aa[:]
print('aa:', aa)
print('bb:', bb)
print('aa == bb:', aa == bb)
# Poniższa komenda ("id") sprawdza czy obie listy są zapisane
# na tym samym adresie pamięci, tzn. czy są tym samym obiektem
print('id(aa) == id(bb):', id(aa) == id(bb))
# Analogicznie działa funnkcja:
print('aa is bb:', aa is bb)
# Kopia przez slicing jest kopią płytką (shallow copy),
# Tzn kopiuje tylko wartości przypisane do indeksów listy.
# Jeżeli, do któregoś indeksu jest przypisana jest referencja
# do edytowalnego (mutable) obiektu jak np. lista,
# to kopia przenosi referencje nie tworzy nowej listy
bb[1].append(3)
bb[0] = 'a'
print('aa:', aa)
print('bb:', bb)
