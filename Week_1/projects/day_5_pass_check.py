import string

pas = 'Sulochana7386yb'

u = string.ascii_uppercase
l = string.ascii_lowercase
sp = string.punctuation
n = list(range(10))

# print([ch in pas for ch in u])

ml = True if len(pas)>8 else False
is_u = any([ch in pas for ch in u])
is_l = any([ch in pas for ch in l])
is_sp = any([ch in pas for ch in sp])
is_n = any([str(ch) in pas for ch in n])

if ml:
    if is_l:
        if is_u:
            if is_sp:
                print('Strong Password')
            else:
                print('Weak password special character missing')
        else:
            print('Weak password uppercase character missing')
    else:
        print('Weak password lowercase character missing')
else:
    print('minimum password length should be 8 characters')

# if is_l and is_sp and is_u and ml:
#     print('Strong password')
# else:
#     print('Weak password')