import math

incoming = ""
while incoming != "stop":
    try:
        incoming = raw_input("Wpisz liczbe: ")
        x = float(incoming)
        print(x, math.pow(x,3))
    except ValueError:
        if(incoming != "stop"):
            print("Blad! Wpisz liczbe!")
