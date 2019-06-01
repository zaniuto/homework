# Znajdź wszystkie samogłoski w podanym niżej stringu
a = "Zażółć gęślą jaźń."

# vowels = ['a', 'o', 'i', 'e', 'u', 'y', 'ą', 'ę', 'ó']
vowels = 'aeiouyąęó'
found_vowels = []

ii = 0
a_len = len(a)
while ii < a_len:
    if a[ii] in vowels:
        found_vowels.append(a[ii])
    ii += 1
print(found_vowels)
