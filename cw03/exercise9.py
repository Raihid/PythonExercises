L = [[],[4],(1,2),[3,4],(5,6,7)]
Result = []
for k in L:
    Result += [e for e in k]
print(Result)
