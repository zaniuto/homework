# napisz funkcję, która zapisuje podaną zmienną na koniec pliku,
# kończąc każdą linijkę znakiem nowej lini
def write_line(file_name, var_to_write):

    with open(file_name, 'a') as _file:
        _file.write(str(var_to_write) + '\n')

write_line('zad_4.txt', 'nowa linia')
write_line('zad_4.txt', '\n\n\n\n\n\n\n')
write_line('zad_4.txt', 1)