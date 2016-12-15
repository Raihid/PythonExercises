import random

def generate_num(L, n=100, k=10):
    L = [random.randint(k) for _ in range(n)]


def linear_find_all(haystack, needle):
    return [idx for idx, val in enumerate(haystack) if val == needle]

L = []
generate_num(L)
linear_find_all(L, random.randint(10))

def binary_find_recur(L, left, right, y):
    if left == right:
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


def median_sort(L, left, right):  # TODO: Potestować
    sorted_list = sorted(L[left:right])
    center = len(sorted_list/2.0) - 1
    if center.is_integer():
        return sorted_list[center]
    else
        return (sorted_list[center.floor()] + sorted_list[center.ceil()])/2

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


def mode_py(L, left, right): # TODO: A czy to dziala?
    reps = {}
    for k in L:
        reps[k] = reps.get(k, 0) + 1
    return max(reps.items(), key=lambda tup: tup[1])

def lider_py(L, left, right):
    reps = {}
    for k in L:
        reps[k] = reps.get(k, 0) + 1
    potential_leader = max(reps.items(), key=lambda tup: tup[1])
    return potential_leader if potential_leader["reps"] > (right-left)/2
           else None
