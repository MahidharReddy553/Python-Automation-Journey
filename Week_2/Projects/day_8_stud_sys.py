def get_stud_data(path):
    with open(path) as f:
        t = f.readlines()
    t1 = []
    for i in t:
        sd = i.split(',')
        t1.append({'name' : sd[0].strip(), 'marks' : int(sd[1].strip())})
    return t1

def get_max_marks(d):
    m = d[0]['marks']
    for i in d:
        if i['marks'] > m:
            m = i['marks']
    return m

def get_name_by_marks(d, m):
    ms = []
    for i in d:
        if i['marks'] == m:
            ms.append(i)
    return ms

def add_data(path, name, marks):
    with open(path, 'a') as f:
        f.write(name+', '+marks+'\n')

    return name, marks

def search_stud(d, name):
    for i in d:
        if i['name'] == name.strip():
            return i
        
def update_marks(path, name, u_marks):
    d = get_stud_data(path)
    us = 0
    for i in d:
        if i['name'] == name:
            i['marks'] = u_marks
            us = i
    with open(path, 'w') as f:
        for i in d:
            f.write(i['name']+', '+str(i['marks'])+'\n')
    return us

def delete_stud(path, name):
    d = get_stud_data(path)
    ds = []
    for i in d:
        if i['name'] == name:
            d.remove(i)
            ds = i
    with open(path, 'w') as f:
        for i in d:
            f.write(i['name']+', '+str(i['marks'])+'\n')
    return ds

def average_marks(d):
    s = 0
    for i in d:
        s += i['marks']
    return round(s / len(d), 2)

def save_data(path, d):
    with open(path, 'w') as f:
        for i in d:
            f.write(i['name']+', '+str(i['marks'])+'\n')
    return d
    


# d = get_stud_data(path)
# add_data(path)



while True:
    path = 'Week_2/Projects/stud_marks.txt'
    d = get_stud_data(path)
    print("""--------------------------------------------------------------------------------------
------------------------------- Student Management System ----------------------------
--------------------------------------------------------------------------------------
          1. View all students
          2. Add student
          3. Search student
          4. Update student marks
          5. Delete student
          6. calculate average marks
          7. Find Topper
          8. Save data
          0. Exit""")
    try:
        c = int(input("Enter your choice(0-8) : "))

        if c == 0:
            break


        elif c == 1:
            print('-----------')
            print('Name | Marks')
            print('----------')
            for i in d:
                print(i['name'], '=', i['marks'])


        elif c == 2:
            name = input("Enter the student's name : ").strip()
            s = search_stud(d, name)
            if not s:
                try:
                    marks = int(input(f"Enter the marks of {name} : ").strip())
                    stud = add_data(path, name, str(marks))
                    print(f"Student with name : '{stud[0]}' and marks : '{stud[1]}' added successfully")
                except ValueError:
                    print("The marks must be an integer")
            else:
                print(f"Student with name : '{name}' already exists !!!")
                print('Try again !!')
                

        elif c == 3:
            name = input("Enter the name of the student you want to search : ").strip()
            stud = search_stud(d, name)
            if stud:
                print('Name :', stud['name'], '\n'+'Marks :', stud['marks'])
            else:
                print(f"No student found with name : {name}")


        elif c == 4:
            name = input("Enter the student name : ")
            s = search_stud(d, name)
            if s:
                marks = input(f"Enter the marks of {name} : ").strip()
                stud = update_marks(path, name, marks)
                print(f"{stud['name']}'s marks updated to marks : '{marks}' successfully")
            else:
                print(f"Student with name : '{name}' not exists !!!")
                print('Try again !!')


        elif c == 5:
            name = input("Enter the student name you want to delete : ")
            s = search_stud(d, name)
            if s:
                stud = delete_stud(path, name)
                print(f"Student with name : '{name}' deleted successfully")
            else:
                print(f"Student with name : '{name}' not exists !!!!")


        elif c == 6:
            if d:
                avg = average_marks(d)
                print(f"The average marks of the class is : {avg}")
            else:
                print("NO students data found")


        elif c == 7:
            ts = get_max_marks(d)
            studs = get_name_by_marks(d, ts)
            if studs:
                if len(studs) == 1:
                    print('The topper of the calss is :')
                    print('Name :', studs[0]['name'])
                    print('Marks :', studs[0]['marks'])
                else:
                    print("The toppers of the class are : ")
                    for i in studs:
                        print('----------------------')
                        print('Name :', i['name'])
                        print('Marks :', i['marks'])
            else:
                print('No data found !!!')


        elif c == 8:
            if d:
                data = save_data(path, d)
                print('the data saved successfully in the file !!!')

            else:
                print('No data is found !!')

    except ValueError:
        print("The choice must be an integer")