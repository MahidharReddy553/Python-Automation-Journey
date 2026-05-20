s = 'cricket and swimming'

def count_v(s : str):
    cv = 0
    for i in s:
        if i.lower() in ['a', 'e', 'i', 'o', 'u']:
            cv += 1
    return cv

def rev_s(s : str):
    rs = ''
    l = list(s)
    le = 0
    r = len(l)-1
    while le < r:
        l[le], l[r] = l[r], l[le]
        le += 1
        r -= 1
    return ''.join(l)

def is_pali(s : str):
    return s == rev_s(s)

def c_words(s : str):
    return len(s.split())

def char_freq(s : str):
    d = {}
    for i in s:
        if i in d:
            d[i] += 1
        else:
            d[i] = 1
    for i in d:
        print(i, '=', d[i])
    return d

def remove_sp(s : str):
    return s.replace(' ', '')

def long_w(s : str):
    lw = ''
    for i in s.split():
        if len(i) > len(lw):
            lw = i
    return lw

def cap_w(s : str):
    return ' '.join(i.capitalize() for i in s.split())


def swap_vn(s : str):
    d = {'a' : 9, 'e' : 3, 'i' : 1 , 'o' : 0, 'u':2}
    vn = ''
    for i in s:
        if i.lower() in d:
            vn += str(d[i.lower()])
        else:
            vn += i
    return vn

print(swap_vn(s))