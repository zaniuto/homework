# Znajdź wszystkie samogłoski w podanym niżej stringu
a = "Zażółć gęślą jaźń."

# vowels = ['a', 'o', 'i', 'e', 'u', 'y', 'ą', 'ę', 'ó']
vowels = 'aeiouyąęó'
# found_vowels = []
found_vowels_2 = []

# ii = 0
# a_len = len(a)
# while ii < a_len:
for elem in a:
    # elem == a[ii]
    if elem in vowels:
        found_vowels_2.append(elem)
    # if a[ii] in vowels:
    #     found_vowels.append(a[ii])
    # ii += 1
# print(found_vowels)
print(found_vowels_2)
# print(found_vowels == found_vowels_2)
