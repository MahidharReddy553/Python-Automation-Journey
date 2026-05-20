def add(a, b):
    return a + b

def sub(a, b):
    return a - b

def mul(a,b):
    return a * b

def div(a, b):
    return a/b


print("""
1. Add
2. Subtract
3. Multiplication
4. Division
""")

c = input("Enter your choice(1/2/3/4):").lower()
a = int(input("Enter the value of 'a' : "))
b = int(input("Enter the value of 'b' : "))


if int(c) == 1:
    print(add(a, b))

elif int(c) == 2:
    print(sub(a, b))

elif int(c) == 3:
    print(mul(a, b))

elif int(c) == 4:
    print(div(a, b))
