path = 'Week_1/projects/notes.txt'

# with open(path, 'w') as f:
#     f.write("""Employee Database
#             Store:
#             name
#             salary
#             department
#             Print nicely using loops.""")


def add_n(path):
    with open(path, 'a') as f:
        n = input("Enter your note : ")
        f.write('\n' + n)
        return n
    
# print(add_n(path))

def view_n(path):
    with open(path) as f:
        print('---------------------------')
        print('Notes : ')
        print('---------------------------')
        for i,j in enumerate(f.readlines()):
            print(f'{i + 1}.',j.strip())
        print('--------------------------')
