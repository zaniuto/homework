# Ppodane 3 boki trojkata, okresl
# - czy uda sie narysowac trojkata
#   * dl. jednego boku musi byc < dlugosc sumy dwoch pozostalych
#  - czy jest to tr. roznoboczny, rownoramienny czy rownoboczny

bok_a = int(input("Podaj bok a: "))
bok_b = int(input("Podaj bok b: "))
bok_c = int(input("Podaj bok c: "))

if (
    (bok_a + bok_b > bok_c)
    and
    (bok_c + bok_b > bok_a)
    and
    (bok_a + bok_c > bok_b)
):
    if bok_a == bok_b == bok_c:
        print("Podane boki tworzą trójkąt równoboczny.")
    elif bok_a == bok_b or bok_a == bok_c or bok_b == bok_c:
        print("Podane boki tworzą trójkąt równoramienny.")
    else:
        print("Podane boki tworzą trójkąt różnoboczny.")