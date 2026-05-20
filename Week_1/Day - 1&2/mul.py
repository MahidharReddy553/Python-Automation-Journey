t = int(input("Enter the table number: "))

for i in range(1,11):
    print(f"{t} X {i} = {t*i}")
print('-----------------------------------------------------------------------')

def mul_table(t : int):
    for i in range(1,11):
        print(f"{t} X {i} = {t*i}")

