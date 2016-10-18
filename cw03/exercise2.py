# "Zabojcze" linijki wykomentowane.

L = [2, 8, 4, 55]
L = L.sort()
print(L)
# Funkcja List.sort() zwraca None (czyli nic). 
# Dziala na liscie ktora ja wywoluje.

# x, y = 1, 2, 3
# Probujemy przypisac trzy wartosci do dwoch zmiennych
# Gdzie ma pojsc trzecia wartosc? 

X = 1, 2, 3 
# X[1] = 4 
# X to tuple, tuple nie mozna zmieniac


X = [1, 2, 3] 
# X[3] = 4
# Wychodzimy poza zakres listy 

X = "abc"
# X.append("d")
# Do typu string nie mozemy dopisywac kolejnych znakow! 
# Musimy stworzyc nowy string.


# map(pow, range(8))
# Brakuje nam jeszcze jednego argumentu, jako ze pow przyjmuje dwa
# Poprawione przykladowo:
print(map(pow, range(8), range(8)))


