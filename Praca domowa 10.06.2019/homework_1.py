# The Utopian Tree goes through 2 cycles of growth every year.
# Each spring, it doubles in height.
# Each summer, its height increases by 1 meter.

# Laura plants a Utopian Tree sapling with a height of 1 meter at the onset of spring.
# How tall will her tree be after n growth cycles?

# For example, if the number of growth cycles is n=5, the calculations are as follows:

# Period  Height
# 0          1
# 1          2
# 2          3
# 3          6
# 4          7
# 5          14
# 6             15
# 7             30

# cycle = [0, 1, 4, 3, 27]
# answer [1, 2, 7, 6, 32766]




def _utopian (x):
    """Funkcja _utopian wylicza wyokość drzewa w metrach po x cyklach
            do prawidłowego funkcjonowania musisz podać liczbę całkowitą, większą od zera

            1 cykl = 6 miesięcy

            0 cykl wysokośc + 1 m
            1 cykl wysokość x 2
            każdy kolejny cykl parzysty = wysokość  + 1 m
            każdy kolejny cykl nieparzysty = wysokość x 2
            """

    #sprawdzam czy integer i liczba dodatnia (jak nie input wymuszający podanie prawidłowej wartości)
    if x >=0 and isinstance(x, int):
        y = 0
        #obliczenia
        while y != x + 1:
            if y == 0:
                wynik = 1
                y = y +1
            elif x != 0:
                if y % 2 == 0:
                    wynik = wynik + 1
                    y = y +1
                elif y % 2 == 1:
                    wynik = wynik * 2
                    y = y +1
        #podanie wyniku
        print ('Po',x ,'cyklach wysokość drzewa wyniesie: ',wynik, 'm.')
    else:
        x = input ("Wprowadź dodatnią całkowitą liczbę cykli")



_utopian(9)


