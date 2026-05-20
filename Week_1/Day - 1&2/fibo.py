a = 0
b = 1

for i in range(5):
    print(a,end = ' ')
    a, b = b, a+b
print()

def fibo_s(n):
    a = 0
    b = 1
    for i in range(5):
        yield a
        a, b = b, a+b

for i in fibo_s(5):
    print(i, end=' ')