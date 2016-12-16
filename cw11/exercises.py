#!/usr/bin/python
import random
import time


# Exercise 11.1
def generate_int(num=10, max_val=20):
    return [random.randint(max_val) for _ in range(num)]


def generate_shuffled(num=10):
    return random.sample([i for i in range(num)], num)


def generate_almost_sorted(num=10):
    return [i + 3*(random.random() - 0.5) for i in range(num)]


def generate_almost_reverse(num=10):
    return reversed(generate_almost_sorted(num))


def generate_gauss(num=10):
    return [random.gauss(0, 5) for _ in range(num)]


def generate_repeated(num=10, max_val=5):
    return [random.randint(max_val) for _ in range(num)]


def cmp(x, y):
    if x < y:
        return -1
    else:
        return x != y


def wrapper(func, *args, **kwargs):
    def wrapped():
        return func(*args, **kwargs)
    return wrapped


# Exercise 11.3
def swap(L, a, b):
    a = int(a)
    b = int(b)
    L[a], L[b] = L[b], L[a]


def selectsort(L, left, right, compare=cmp):
    for i in range(left, right):
        k = i
        for j in range(i+1, right+1):
            if compare(L[j], L[k]) < 0:
                k = j
        swap(L, i, k)


def insertsort(L, left, right, compare=cmp):
    for i in range(right, left, -1):
        if L[i-1] > L[i]:
            swap(L, i-1, i)
    for i in range(left+2, right+1):
        j = i
        item = L[i]
        while compare(item, L[j-1]) < 0:
            L[j] = L[j-1]
            j = j-1
        L[j] = item


def bubblesort(L, left, right, compare=cmp):
    for i in range(left, right):
        for j in range(left, right-i):
            if compare(L[j], L[j+1]) < 0:
                swap(L, j+1, j)


def quicksort(L, left, right, compare=cmp):
    if left >= right:
        return
    swap(L, left, (left + right) / 2)
    pivot = left
    for i in range(left + 1, right + 1):
        if L[i] < L[left]:
            pivot = pivot + 1
            swap(L, pivot, i)
    swap(L, left, pivot)
    quicksort(L, left, pivot - 1)
    quicksort(L, pivot + 1, right)


# Exercise 11.4
def test_times(magnitude):
    algorithms = {"selectsort": selectsort, "insertsort": insertsort,
                  "bubblesort": bubblesort, "quicksotrt": quicksort}
    data_sizes = [10 ** k for k in range(magnitude)]
    for N in data_sizes:
        print("We're testing for sample N=" + str(N))
        for name, algo in algorithms.items():
            L = generate_shuffled(N)
            t1 = time.time()
            try:
                algo(L, 0, N-1)
            except RecursionError:
                print(name + ": RecursionError!")
                continue
            t2 = time.time()
            print(name + ": " + str(t2 - t1))


# Exercise 11.5
def bogosort(L, left, right):
    """An example of ineffective sorting algorithm with time complexity of
    O((n+1)!).
    """
    while not all(L[i] <= L[i+1] for i in range(left, right-1)):
        random.shuffle(L)

L = [1, 3, 2, -2]
print(L)
bogosort(L, 0, 4)
print(L)
