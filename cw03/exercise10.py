
val = { "M" : 1000, "D": 500, "C": 100, \
            "L": 50, "X": 10, "V": 5, "I": 1}

def roman2int(roman):
    prev_char = roman[0]
    value = val[prev_char]
    for s in roman[1:]:
        if(val[s] <= val[prev_char]):
            value += val[s]
        else:
            value += val[s] - 2*val[prev_char]
        prev_char = s
    return value


print(val["C"])
print(roman2int("CMXCIX"))
    
