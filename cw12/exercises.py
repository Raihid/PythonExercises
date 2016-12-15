import random
import math

def generate_num(L, n=100, k=10):
    L += [random.randint(0, k) for _ in range(n)]

def generate_sorted(L, n=100, k=10):
    L += [random.randint(0, k)]
    for i in range(1, n):
        L += [random.randint(0, k) + L[i-1]]


def linear_find_all(haystack, needle):
    return [idx for idx, val in enumerate(haystack) if val == needle]

L = []
generate_num(L)
print(linear_find_all(L, random.randint(0, 10)))


def binary_find_recur(L, left, right, y):
    if right - left <= 1:
        if L[left] == y:
            return left
        else:
            raise ValueError("Value not found!")

    center = (right + left) / 2
    if L[center] == y:
        return center
    elif y > L[center]:
        return binary_find_recur(L, center, right, y) 
    else:
        return binary_find_recur(L, left, center, y) 

L = []
generate_sorted(L, 100, 10)
for k in L:
    try:
        binary_find_recur(L, 0, 100, k)
    except ValueError as ve:
        print(ve)

def median_sort(L, left, right):
    sorted_list = sorted(L[left:right])
    center = (len(sorted_list) - 1)/2.0
    print(center)
    if center.is_integer():
        return sorted_list[int(center)]
    else:
        return (sorted_list[int(center)] + sorted_list[int(center + .5)])/2.0

L = []
generate_num(L, 30, 20)
L = [1, 2, 3, 4]
print(median_sort(L, 0, 4))


def mode_sort(L, left, right): # TODO: Czy to dziala?!!
    sorted_list = sorted(L[left:right])
    current = {"reps": 1, "val": sorted_list[0]}
    best = current.copy()
    for k in L[1:]:
        if k != current["val"]:
            if best["reps"] < current["reps"]:
                best = current.copy()
            current["val"] = k
            current["reps"] = 1
        else:
            current["reps"] += 1
    return best

L = [1, 2, 3, 5, 5, 5, 5, 5, 5, 7, 8]
print(mode_sort(L, 0, len(L)))

def mode_py(L, left, right): # TODO: A czy to dziala?
    reps = {}
    for k in L:
        reps[k] = reps.get(k, 0) + 1
    return max(reps.items(), key=lambda tup: tup[1])

L = [1, 2, 3, 5, 5, 5, 5, 5, 5, 7, 8]
print(mode_py(L, 0, len(L)))

def lider_py(L, left, right):
    reps = {}
    for k in L:
        reps[k] = reps.get(k, 0) + 1
    leader = max(reps.items(), key=lambda tup: tup[1])
    return leader if leader[1] > (right-left-1)/2 + 1 else None

L = [1, 2, 3, 5, 5, 5, 5, 5, 5, 5, 7, 8]
print(len(L))
print(lider_py(L, 0, len(L)))

