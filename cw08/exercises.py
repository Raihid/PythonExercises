#!/usr/bin/python
import random
from math import sqrt


# ----- Exercise 1 -----
def solve1(a, b, c):
    """Solving linear equation a x + b y + c = 0."""
    if a == 0 and b == 0:
        if c == 0:
            print("Equation is satisified by all real numbers (x, y)")
        else:
            print("Impossible equation " + str(c) + " == 0 ")
    elif b == 0:
        x = -c/a
        print("x = " + str(x))
    elif a == 0:
        y = -c/b
        print("y = " + str(y))
    else:
        coeff_b = -(b*1.0/a)
        coeff_c = -(c*1.0/a)
        solution = "x = " + str(coeff_b) + "*y"
        if c != 0:
            solution += " + " if coeff_c > 0 else " - "
            solution += str(abs(coeff_c))
        print(solution)


solve1(8, 2, 2)
solve1(5, 1, 0)
solve1(0, 2, 0)
solve1(0, 0, 0)
solve1(0, 0, 5)


# ----- Exercise 2 -----
def solve2(a, b, c):
    delta = sqrt(b*b - 4*a*c)
    if a == 0:
        solve1(0, b, c)
    elif delta == 0:
        print("Solution is " + str(-b/(2.0*a)))
    elif delta > 0:
        print("Solutions are " + str([(-b-delta)/(2.0*a), (-b+delta)/(2.0*a)]))
    else:
        print("No real number solutions")


solve2(0, 5, 3)
solve2(1, 5, 3)
solve2(2, 4, 2)


# ----- Exercise 3 -----
def calc_pi(n=100):
    hit = 0
    for i in range(0, n):
        x = random.uniform(0, 1.0)
        y = random.uniform(0, 1.0)
        if x*x + y*y <= 1:
            hit += 1
    return 4.0*hit/n


print(calc_pi())
print(calc_pi(10000))


# ----- Exercise 4 -----
def heron(a, b, c):
    if a > b + c or b > a + c or c > a + b:
        raise ValueError
    s = (a+b+c)/2.0
    return sqrt(s*(s-a)*(s-b)*(s-c))

print(heron(5, 5, 5))
print(heron(7, 10, 5))
print(heron(6, 12, 6))
try:
    print(heron(6, 12.5, 6))
except ValueError:
    print("Triangle inequality works")


# ----- Exercise 5 -----
def ackermann(n, p):
    """Funkcja Ackermanna, n i p to liczby naturalne.
    Zachodzi A(0, p) = 1, A(n, 1) = 2n, A(n, 2) = 2 ** n,
    A(n, 3) = 2 ** A(n-1, 3).
    """
    if n == 0:
        return 1
    if p == 0 and n >= 0:
        if n == 1:
            return 2
        else:
            return n + 2
    if p >= 0 and n >= 1:
        return ackermann(ackermann(n-1, p), p-1)


def examine_ackermann():
    results = {}
    for p in range(1, 5):
        results[p] = {}
        for n in range(1, 15):
            try:
                results[p][n] = ackermann(n, p)
            except RecursionError:
                break
    return results

print("----- Ackermann -----\nBlack spaces mean max recursion exceeded")
data = examine_ackermann()
table = "|".join([str(i).rjust(4) for i in data[1].keys()])
table = "p\\n|" + table
for p, row in data.items():
    table += "\n" + str(p).ljust(3) + "|"
    table += "|".join(str(item).rjust(4) for key, item in row.items())
print(table)


# ----- Exercise 6 -----
def dynamic_P(n, m):
    P = {i: {0: 0} for i in range(1, n+1)}
    P[0] = {0: 0}
    for j in range(1, m+1):
        P[0][j] = 1.0

    for i in range(1, n+1):
        for j in range(1, m+1):
            P[i][j] = 0.5*(P[i-1][j] + P[i][j-1])
    return P[n][m]


def recursive_P(i, j):
    if i == 0 and j == 0:
        return 0.5
    elif j == 0:
        return 0.0
    elif i == 0:
        return 1.0
    else:
        return 0.5*(recursive_P(i-1, j) + recursive_P(i, j-1))


print(dynamic_P(5, 11))
print(recursive_P(5, 11))

# By uncommenting these lines we can see, that dynamic version is way, way
# faster than the recursive one.
# print(dynamic_P(10, 21))
# print(recursive_P(10, 21))
