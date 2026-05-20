c_book = [{'name':'bvns', 'number':'8977623456'},
          {'name':'ram', 'number':'8977653456'}]

def add_c():
    name = input("Enter the name : ")
    ph = input("Enter the phone number : ")
    c_book.append({'name':name, 'number':ph})
    return c_book

def search_c():
    n = input("Enter the name of contact you want : ")
    for i in c_book:
        if i['name'] == n:
            return i
        
def del_c():
    name = input("Enter the name of the contact you want to delete: ")
    for i in c_book:
        if i['name'] == name:
            c_book.remove(i)


def display_cb():
    for i in c_book:
        print(i)


while True:
    print('1. Add Contact\n2. Search Contact\n3. Delete Contact\n4. Display Contacts\n5. Quit')
    c = int(input("Enter your choice(1/2/3/4/5) : "))
    if c == 1:
        add_c()
    elif c == 2:
        print(search_c())
        print()
    elif c == 3:
        del_c()
    elif c == 4:
        display_cb()
    elif c == 5:
        break
    else:
        print("Invalid choice!! please enter 1/2/3/4/5")