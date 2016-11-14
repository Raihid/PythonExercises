def flatten(seq):
    if(isinstance(seq, (list, tuple))):
        L = []
        for i in seq:
           L += flatten(i)
        return L
    else:
        return [seq]

seq = [1,(2,3),[["a"]],[4,(5,6,7)],8,[9]]
print(flatten(seq))


