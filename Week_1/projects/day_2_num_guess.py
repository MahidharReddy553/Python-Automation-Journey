import random as r

n = r.randint(1,100)
a = 0

while True:
    un = int(input("Guess the number: "))
    a += 1
    if un > n:
        print("The number is too large")
    if un < n:
        print("The number is too small")
    if un == n:
        print(f"correct! You guessed in {a} attempts.")
        break
