p = 'Week_1/sample.txt'


def read_f(path):
    with open(path, 'r') as f:
        t = f.readlines()
        print(t)


def write_f(path):
    with open('Week_1/sw_d.txt', 'w') as f:
        text = 'there is no tomorrow\nhard work beats talent when talent does not work hard\nAs above, so below'
        f.write(text)

def append_f(path):
    with open(path, 'a') as f:
        f.write('\nThe best time to start is NOW.')

def count_wf(path):
    with open(path) as f:
        t = f.read()
        wl = t.split()
        return len(wl)

def count_lf(path):
    with open(path) as f:
        tl = f.readlines()
        return len(tl)
    

def search_f(path,s):
    with open(path) as f:
        t = f.read()
        if s in t:
            return 'exists'
        else:
            return 'not exist'
        
        
def copy_f(path, cpath):
    f = open(path)
    t = f.read()
    f.close()
    with open(cpath,'w') as cf:
        cf.write(t)
    
def replace_wf(path):
    with open(path, 'r') as f:
        t = f.read()
        t = t.replace('now', 'NOW')
    with open(path, 'w') as f:
        f.write(t)
        return t
    

print(replace_wf(p))