def fibonacci(n):
    if(n < 0):
        return -1 # error
    if(n == 0):
        return 0
    if(n == 1 or n == 2):
        return 1
    val1 = 1; val2 = 1;
    for i in range(2,n):
        val2, val1 = val1 + val2, val2
    return val2
            

print(fibonacci(15))
