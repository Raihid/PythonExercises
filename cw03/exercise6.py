dim = { "w" : 4, "h" : 2 }  # size of a single square/rectangle
num_sq = { "line": 6, "row": 2 } # num of squares in row

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
print(rectangle)
