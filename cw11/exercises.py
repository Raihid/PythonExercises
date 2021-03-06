#!/usr/bin/python
import random
import time


# Exercise 11.1
def generate_int(num=10, max_val=20):
    return [random.randint(max_val) for _ in range(num)]


# Exercise 11.1a
def generate_shuffled(num=10):
    return random.sample([i for i in range(num)], num)


# Exercise 11.1b
def generate_almost_sorted(num=10):
    return [i + 3*(random.random() - 0.5) for i in range(num)]


# Exercise 11.1c
def generate_almost_reverse(num=10):
    return reversed(generate_almost_sorted(num))


# Exercise 11.1d
def generate_gauss(num=10):
    return [random.gauss(0, 5) for _ in range(num)]


# Exercise 11.1e
def generate_repeated(num=10, max_val=5):
    return [random.randint(max_val) for _ in range(num)]


def cmp(x, y):  # Simple fix for Python 3
    if x < y:
        return -1
    else:
        return x != y


def wrapper(func, *args, **kwargs):
    def wrapped():
        return func(*args, **kwargs)
    return wrapped


# Exercise 11.2 omitted, because my final project does a lot of gnuplotting.


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
    algorithms = {"selectsort": {"call": selectsort, "quick": False},
                  "insertsort": {"call": insertsort, "quick": False},
                  "bubblesort": {"call": bubblesort, "quick": False},
                  "quicksort": {"call": quicksort, "quick": True}}
    data_sizes = [10 ** k for k in range(magnitude)]
    for N in data_sizes:
        print("We're testing for sample N=" + str(N))
        for name, algo in algorithms.items():
            if N >= 1e5 and not algo["quick"]:  # O(n^2) is taking too long
                continue
            L = generate_shuffled(N)
            t1 = time.time()
            algo["call"](L, 0, N-1)
            t2 = time.time()
            print(name + ": " + str(t2 - t1))
        print("--------")

test_times(4)  # Any higher value makes slower sorts go on forever
# More values in comparison.txt


# Exercise 11.5
def bogosort(L, left, right):
    """An example of ineffective sorting algorithm with time complexity of
    O((n+1)!). It shuffles the array until it is sorted. Because of that even
    for 10 numbers sorting may take several seconds.
    """
    while not all(L[i] <= L[i+1] for i in range(left, right-1)):
        random.shuffle(L)

L = [1, 3, 2, -2]
print("Before bogosort" + str(L))
bogosort(L, 0, 4)
print("After bogosort" + str(L))

N = 7  # Very slow for higher values
L = generate_shuffled(N)
print("Before bogosort" + str(L))
bogosort(L, 0, N)
print("After bogosort" + str(L))
