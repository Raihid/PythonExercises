import math

incoming = ""
while incoming != "stop":
    try:
        incoming = raw_input("Enter number: ")
        x = float(incoming)
        print(x, math.pow(x,3))
    except ValueError:
        if(incoming != "stop"):
            print("Error! Enter a number")
