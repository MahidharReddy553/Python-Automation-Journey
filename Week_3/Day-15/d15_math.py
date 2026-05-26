def square(n : int):
    return n * n

def sum_n(n : int):
    s = (n*(n+1))//2
    return s

def is_prime(n : int):
    if n == 2:
        return True
    for i in range(2, n//2):
        if n%i == 0:
            return False     
    return True

def fact(n : int):
    if n == 0 or n == 1:
        return 1
    # f = 1
    # while n and n != 1:
    #     f *= n
    #     n -= 1
    #     print(n)
    # return f
    
    return n * fact(n-1)