zdanie = "Ala ma kota, kot ma Ale."
zdanie2 = ' Ale ja "wolę" psy!'

# Stringi można do siebie dodać tworząc w ten sposób nowy string
print(zdanie + zdanie2)
# W przypadku wypisywania wielu stringów domyślnie są one łączone spacją
# Każdę wypisanie stringa funkcją print końćzy się dodaniem znaku '\n', czyli przejścia do nowej lini
print(zdanie, zdanie2)

# Można jednak zastąpić znak końca lini innym stringiem
print(zdanie, end='____')
print(zdanie2)
