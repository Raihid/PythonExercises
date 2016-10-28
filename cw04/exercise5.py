def reverse_recursive(L, left, right):
    if(left == right):
        return
    else:
        center = (left+right)/2
        reverse_recursive(L, left, center)
        reverse_recursive(L, center+1, right)
        L[center+1:right+1], L[left:center+1] = L[left:center+1], L[center+1:right+1]

def reverse_iter(L, left, right):
    pivot = (right-left)/2 + 1
    for i in range(0, pivot):
        L[right-i], L[left+i] = L[left+i], L[right-i]

L1 = [1, 2, 3, 4, 5, 6, 7, 8]

reverse_recursive(L1, 0, len(L1)-1)
print(L1)

L2 = ["a", "b", "c", "d", "e", "f"]
reverse_iter(L2, 2, 5)
print(L2)
