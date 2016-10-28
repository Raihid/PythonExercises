def factorial(n):
    if n < 0:
        return -1 # error
    val = 1;
    for i in range(1,n+1):
        val *= i
    return val

print(factorial(8))
