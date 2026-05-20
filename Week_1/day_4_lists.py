l = [46, 96, 69, 45, 68, 68]

def l_max(l : list):
    e = l[0]

    # for i in range(1, len(l)):
    #     if l[i] > e:
    #         e = l[i]

    for i in l[1:]:
        if i > e:
            e = l
    return e

def l_min(l: list):
    e = l[0]
    for i in l[1:]:
        if i < e:
            e = i
    return e

def l_sum(l : list):
    s = 0
    for i in l:
        s += i

    return s

def l_ceo(l : list):
    e = 0
    o = 0

    for i in l:
        if i%2 == 0:
            e += 1
        else:
            o += 1

    return e,o


def l_rev(l : list):
    n = len(l)
    le = 0
    r = n - 1

    while le < r:
        l[le], l[r] = l[r], l[le]
        le += 1
        r -= 1
    return l

def l_rdup(l : list):
    li = []
    for i in l:
        if i not in li:
            li.append(i)
    return li

def l_sort(l : list):
    print(l)
    print('----------------')
    for i in range(len(l)):
        print('============================')
        for j in range(i+1, len(l)):
            print(i, j)
            if l[i] > l[j]:
                l[i], l[j] = l[j], l[i]
                print(l)
                
        print('===========================')
    return l

def l_slar(l : list):
    la = l[0]
    sl = l[0]

    for i in l:
        if i > la:
            sl = la
            la = i
        elif i > sl:
            sl = i
        else:
            continue
    return sl

print(l_sort(l))