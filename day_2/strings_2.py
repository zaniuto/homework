# Znak backslash "\" może zamienić następny znak w znak specjalny
# np. "\n" to znak nowej linii, a string "\t" interpretowany jest jako znak tabulacji
moj_plik = "C:\teamwork\nowy_folder\skrypt.py"
print(moj_plik)

# Aby zapobiec interpretowania backslasha należy go pwotórzyć "\\"
moj_plik2 = "C:\\teamwork\\nowy_folder\\skrypt.py"
print(moj_plik2)

# Możliwe jest także poprzedzenie stringu literą "r",
# co zmienia string w "raw-string", czyli string nie intrpretowany, znaki wypisywane są "dosłownie"
moj_plik3 = r"C:\teamwork\nowy_folder\skrypt.py"
print(moj_plik3)
