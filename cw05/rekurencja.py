#!/usr/bin/python
# Exercise 5.1


def factorial(n):
    val = 1;
    for i in range(1,n+1):
        val *= i
    return val

def fibonacci(n):
    val1 = 1; val2 = 1;
    if(n == 1 or n == 2):
        return 1
    for i in range(2,n):
        tmp = val2
        val2 = val1 + val2
        val1 = tmp
    return val2
