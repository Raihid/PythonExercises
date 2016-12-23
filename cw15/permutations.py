#!/usr/bin/python
N = 8


# Exercise 15.1
def factorize(num):
    factors = []
    i = 2
    while i <= num:
        if num % i == 0:
            factors += [i]
            num /= i
        else:
            i += 1
    return factors


def mul_perm(perm1, perm2):        # perm1*perm2
    N = len(perm1)
    if N != len(perm2):
        raise ValueError("Perms have different sizes!")
    out_perm = [None] * N
    for i in range(N):
        out_perm[i] = perm1[perm2[i]]
    return out_perm


def invert_perm(perm):
    out_perm = [None] * len(perm)
    for i, k in enumerate(perm):
        out_perm[k] = i
    return out_perm


def is_identity(perm):
    return all(perm[i] == i for i in range(len(perm)))


def find_order(perm):
    order = 0
    tmp_perm = perm
    while not is_identity(tmp_perm):
        tmp_perm = mul_perm(tmp_perm, perm)
        order += 1
    return order


identity = range(N)
shift = [(i + 1) % N for i in range(N)]

print("----- Testing functions for permutations -----")
print("Inversion of {}: {}".format(shift, invert_perm(shift)))
print("Is range(N) identity: {}".format(is_identity(identity)))
print("What is the order of {}: {}".format(shift, find_order(shift)))


# Exercise 15.3
def generate_cyclic(N):
    factors = factorize(N)
    if not factors:
        factors = [N]

    perm = []
    for factor in factors:
        start = len(perm)
        perm += [start + (i + 1) % factor for i in range(0, factor)]

    group = [perm]
    tmp_perm = perm
    while not is_identity(tmp_perm):
        tmp_perm = mul_perm(tmp_perm, perm)
        group += [tmp_perm]
    return group


print("----- Testing  for permutations -----")
p_1 = generate_cyclic(5)
print("For N = {}, our group nas {} elements: {}".format(5, len(p_1), p_1))
p_2 = generate_cyclic(6)
print("For N = {}, our group nas {} elements: {}".format(6, len(p_2), p_2))
p_3 = generate_cyclic(11)
print("For N = {}, our group nas {} elements: {}".format(11, len(p_3), p_3))
