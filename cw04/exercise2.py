
# parametry

def get_ruler(unit, length):
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
    return ruler

def get_squares(line, row):
    dim = { "w" : 4, "h" : 2 }  # size of a single square/rectangle
    num_sq = { "line": line, "row": row } # num of squares in row

    width = dim["w"] * num_sq["line"];
    height = dim["h"] * num_sq["row"];

    rectangle = "";
    for i in range(0, height+1):
        for j in range(0, width+1):
            if i % dim["h"] == 0:
                rectangle += ("+" if j % dim["w"] == 0 else "-")
            else: 
                rectangle += ("|" if j % dim["w"] == 0 else " ")
        rectangle += "\n"
    return rectangle

print(get_ruler(5, 71))
print(get_squares(6, 2))

