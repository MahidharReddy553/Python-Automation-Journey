from d15_calc import *

while True:
    # print("""
    # 1. Add
    # 2. Subtract
    # 3. Multiplication
    # 4. Division
    # 0. Exit
    # """)

    # c = input("Enter your choice(1/2/3/4):").lower()
    c = 0
    if int(c) == 0:
        break
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
    else:
        print('Invalid Choice !!!')

import d15_str_utils as strutils

s = "cricket and swimming"
# print(strutils.char_freq(s))
# print(strutils.count_v(s))
print(strutils.c_words(s))
# print(strutils.cap_w(s))
# print(strutils.is_pali(s))
# print(strutils.rev_s(s))

import d15_math as mutils

print(mutils.fact(6))
print(mutils.square(7))
print(mutils.sum_n(10))