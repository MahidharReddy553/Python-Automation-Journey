d = {'name':'bvns/pb', 'age':76, 'marks':96}
d1 = {'name':'happy', 'age': 7, 'marks':1000}

def print_dict(d : dict):
    for i, j in d.items():
        print(i, '=', j)

s = "betty bought a better butter to make the bitter butter better"

def word_freq(s : str):
    wl = s.split()
    fd = {}
    for w in wl:
        if w in fd:
            fd[w] += 1
        else:
            fd[w] = 1
    return fd


def merge_dicts(d1 : dict, d2 : dict):
    return d1 | d2

marks = {
    "A": 90,
    "B": 75,
    "C": 95
}

def max_value(d : dict):
    m = 0
    k = 0
    for key,value in d.items():
        if value > m:
            m = value
            k = key
    return k
    
emps = [{'name':'bvns', 'salary':90000, 'Dept':'ML Ops'},
        {'name':'ram', 'salary':100000, 'Dept':'ML Ops Lead'},
        {'name':'ybmr', 'salary':145000, 'Dept':'QA Testing'}]

def pretty_print(e : list):
    print('---------------------------------------------------')
    print('Employee database')
    print('-------------------------------------------------------')
    print(' name   salary  department')
    for i in e:
        print('|',i['name'],'|',i['salary'],'|',i['Dept'],'|')
    print('------------------------------------------------------------')

def rem_dups(s : str):
    d = word_freq(s)
    n = d.keys()
    return ' '.join(n).strip()


store = { "pen": 10, "book": 5 }


def inventory(d : dict):
    pens = int(input("Enter the number of pens you want : "))
    books = int(input("Enter the number of books you want : "))
    d['pen'] -= pens
    d['book'] -= books
    return d



def indexed_dict(s : str):
    sl = s.split()
    d = {}
    for i in range(1, len(sl)+1):
        d[i] = sl[i-1]
    return d

print(indexed_dict('i love python'))