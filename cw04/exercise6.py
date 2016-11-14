def sum_seq(item):
    if(not isinstance(item, (list, tuple))):
        try:
            val = float(item)
            return val
        except:
            return 0
    return sum(sum_seq(s) for s in item)

L = [5, 7, (2, [2.5, 5.0])]
print(sum_seq(L))
