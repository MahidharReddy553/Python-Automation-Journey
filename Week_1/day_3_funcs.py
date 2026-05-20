def square(n : int):
    return n * n

def is_prime(n : int):
    if n == 2:
        return True
    for i in range(2, n//2):
        if n%i == 0:
            return False     
    return True

def rev_s(s : str):
    return s[::-1]

def count_v(s : str):
    c = 0
    for i in s:
        if i in ['a', 'e', 'i', 'o', 'u']:
            c += 1
    if not c:
        return "Given string has no vowels"
    return c

def fact(n : int):
    if n == 0 or n == 1:
        return 1
    f = 1
    while n and n != 1:
        f *= n
        n -= 1
        print(n)
    return f
    
    # return n * fact(n-1)

def is_pali(s : str):
    if type(s)!= str:
        return 'Given input is not a string'
    return s == s[::-1]












# p = 0
# print(n, p)

# u = n % 10
# p = p * 10 + u
# n = n // 10

# print(n, p)

# u = n % 10
# p = p * 10 + u
# n = n // 10

# print(n, p)

# u = n % 10
# p = p * 10 + u
# n = n // 10

# print(n, p)



# n = 121212121212
# n1 = n
# p = 0
# print(n, p)
# while n:
    
#     u = n % 10
#     p = p * 10 + u
#     n = n//10
#     print(n, p)

# print(p == n1)