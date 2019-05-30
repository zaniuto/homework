# https://pl.wikipedia.org/wiki/Rok_przest%C4%99pny#Historia
# oblicz czy rok jest przestępny
# czyli, podzielny przez 4, nie podzielny przez 100 ale podzielny przez 400

x = int(input("Podaj rok: "))
# if x % 400 == 0:
#     print("Podany rok jest przestępny!")
# elif x % 4 == 0 and x % 100 != 0:
#     print("Podany rok jest przestępny!")
# else:
#     print("Podany rok nie jest przestępny!")

if (
    x % 400 == 0
    or (x % 4 == 0 and x % 100 != 0)
):
    print("Podany rok jest przestępny!")
else:
    print("Podany rok nie jest przestępny!")

