# parametry
unit = 5
length = 71


ruler = ""
for i in range(0, length): # pierwsza linia
    if i % unit == 0:
        ruler += "|"
    else:
        ruler += "."
ruler += "\n"
i = 0

ruler += "0"
for i in range (1, length/unit+1): # druga linia
    ch = str(i)
    ruler += " " * (unit-len(ch)) + ch

print(ruler)

