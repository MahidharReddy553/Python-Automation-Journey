t = tuple(i*i for i in range(1, 11))
print('tuple :', t)
print('length of tuple :', len(t))

def is_prime(n):
    if n == 1:
        return False
    for i in range(2, n//2 + 1):
        if n % i == 0:
            return False
    return True

p = {i for i in range(1, 50) if is_prime(i)}
e = {i for i in range(2, 50, 2)}
o = {i for i in range(1, 50, 2)}

print('primes :', p)
print('odds :', o)
print('intersection of primes and odds :', p.intersection(o))
print('Union of evens and odds :', e.union(o))
print('is evens subset of odds :', e.issubset(o))
