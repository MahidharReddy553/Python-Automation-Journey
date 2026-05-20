s = input("Enter the string: ")

c = 0
for i in s:
    if i in ['a', 'e', 'i', 'o', 'u']:
        c += 1

print(c)
