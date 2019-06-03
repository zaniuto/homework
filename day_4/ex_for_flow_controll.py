# w pętli for działa również instrukcja "break" (przerwanie wykonywania pętli)
for ii in range(10):
    if ii % 5 == 3:
        break
    print(ii)
# oraz "continue" (natychmiast przejdź do kolejnej iteracji)
for ii in range(10):
    if ii % 5 == 0:
        continue
    print(ii)