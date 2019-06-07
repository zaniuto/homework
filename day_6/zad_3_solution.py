# wczytaj 3 pierwsze linijki z pliku z nazwą zapisaną pod zmienną path
# wykorzystując komendę with
path = 'tekst1.txt'

print('ver 1')
with open(path, 'r') as plik:
    for ii in range(3):
        print(plik.readline())

print('ver 2')
with open(path, 'r') as plik:
    for line in plik.readlines()[:3]:
        print(line)