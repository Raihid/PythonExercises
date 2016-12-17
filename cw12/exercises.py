import random


# Simple helper functions
def generate_num(L, n=100, k=10):
    L += [random.randint(0, k) for _ in range(n)]


def generate_sorted(L, n=100, k=10):
    L += [random.randint(0, k)]
    for i in range(1, n):
        L += [random.randint(0, k) + L[i-1]]


# Exercise 12.1
def linear_find_all(haystack, needle):
    return [idx for idx, val in enumerate(haystack) if val == needle]

print("----- Testing linear_find_all -----")
L = []
generate_num(L)
y = random.randint(0, 10)
print("In array: " + str(L) + " we are searching for value " + str(y))
print(linear_find_all(L, random.randint(0, 10)))


# Exercise 12.2
def binary_find_recur(L, left, right, y):
    if right - left <= 1:
        if L[left] == y:
            return left
        else:
            raise ValueError("Value not found!")

    center = int((right + left) / 2)
    if L[center] == y:
        return center
    elif y > L[center]:
        return binary_find_recur(L, center, right, y)
    else:
        return binary_find_recur(L, left, center, y)

print("----- Testing binary_find_recur -----")
L = []
generate_sorted(L, 20, 10)
print("Searching for values in array " + str(L))
for k in L[9:13]:
    try:
        print("Number " + str(k) + " found on position no. " +
              str(binary_find_recur(L, 0, 20, k)))
    except ValueError as ve:
        print(ve)


# Exercise 12.3
def median_sort(L, left, right):
    sorted_list = sorted(L[left:right])
    center = (len(sorted_list) - 1)/2.0
    if center.is_integer():
        return sorted_list[center]
    else:
        return (sorted_list[int(center)] + sorted_list[int(center + .5)])/2.0

print("----- Testing median_sort -----")
L = [1, 2, 3, 4]
print("Searching for median in array " + str(L))
print(median_sort(L, 0, 4))

L = []
generate_num(L, 30, 20)
print("Searching for median in array " + str(L))
print(median_sort(L, 0, 30))


# Exercise 12.4
def mode_sort(L, left, right):
    sorted_list = sorted(L[left:right])
    current = {"reps": 1, "val": sorted_list[0]}
    best = current.copy()
    for k in sorted_list[1:]:
        if k != current["val"]:
            if best["reps"] < current["reps"]:
                best = current.copy()
            current["val"] = k
            current["reps"] = 1
        else:
            current["reps"] += 1
    return best

print("----- Testing mode_sort -----")
L = [1, 2, 3, 5, 5, 5, 5, 5, 5, 7, 8]
random.shuffle(L)
print("Searching for mode in array: " + str(L))
print(mode_sort(L, 0, len(L)))


# Exercise 12.5
def mode_py(L, left, right):
    reps = {}
    for k in L:
        reps[k] = reps.get(k, 0) + 1
    mode = max(reps.items(), key=lambda tup: tup[1])
    return {"val": mode[0], "reps": mode[1]}
print("----- Testing mode_py -----")
L = [1, 2, 3, 5, 5, 5, 5, 5, 5, 7, 8]
random.shuffle(L)
print("Searching for mode in array: " + str(L))
print(mode_py(L, 0, len(L)))


# Exercise 12.6
def leader_py(L, left, right):
    reps = {}
    for k in L:
        reps[k] = reps.get(k, 0) + 1
    leader = max(reps.items(), key=lambda tup: tup[1])
    return leader if leader[1] > (right-left-1)/2 + 1 else None

print("----- Testing leader_py -----")
L = [1, 2, 3, 5, 5, 5, 5, 5, 5, 5, 7, 8]
print("Searching for leader in array " + str(L) + " of length " + str(len(L)))
print(leader_py(L, 0, len(L)))
L = [1, 2, 3, 5, 5, 5, 5, 5, 5, 7, 8]
print("Searching for leader in array " + str(L) + " of length " + str(len(L)))
print(leader_py(L, 0, len(L)))
