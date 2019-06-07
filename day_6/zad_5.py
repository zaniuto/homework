# połącz pliki z listy "list_of_files" w jeden pliku ze zmiennej path
# pliki znajdują się w folderze "zad_5"
path = 'wiersz.txt'

list_of_files = [
    'txt_1.txt',
    'txt_2.txt',
    'txt_3.txt',
    'txt_4.txt',
]

with open(path, 'w') as _file_2:
    for file_path in list_of_files:
        with open(f'zad_5/{file_path}', 'r') as _file:
            line = _file.readline()
            while line:
                _file_2.write(line)
                line =  _file.readline()