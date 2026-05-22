
def fetch_data(path):
    d = []
    with open(path) as f:
        for i in f:
            l = i.strip().split(' - ')
            d.append({'exname' : l[0].strip(), 'examt' : float(l[1].strip())})
    return d


def view_data(data):
    print('-------------------------------------------------------')
    print("Expenses Data")
    print('-------------------------------------------------------')
    print("Expense - Amount")
    print('-------------------------------------------------------')
    for i in data:
        print(i['exname'], '-', i['examt'])
    return data


def add_expense(path, d, name, amt):
    d.append({'exname' : name, 'examt': float(amt)})
    with open(path, 'a') as f:
        f.write(name.capitalize()+' - '+str(amt)+'\n')
    return name, amt


def calculate_exps(d):
    te = 0
    for i in d:
        te += i['examt']
    return te


def search_by_name(name,d):
    for i in d:
        if i['exname'].lower() == name:
            return i
        

def delete_expense(d, name):
    deli = {}
    for i in d:
        if i['exname'].lower() == name:
            d.remove(i)
            deli = i
    with open(path, 'w') as f:
        for i in d:
            f.write(i['exname']+' - '+str(i['examt'])+'\n')
    return deli
        

def filter_data_desc(data):
    sd = data
    for i in range(len(sd)):
        for j in range(i+1, len(sd)):
            if sd[i]['examt'] < sd[j]['examt']:
                sd[i], sd[j] = sd[j], sd[i]
    return sd

def filter_data_asc(data):
    sd = data
    for i in range(len(sd)):
        for j in range(i+1, len(sd)):
            if sd[i]['examt'] > sd[j]['examt']:
                sd[i], sd[j] = sd[j], sd[i]
    return sd

def filter_above_range(data, r):
    sd = []
    for i in data:
        if i['examt'] >= r:
            sd.append(i)
    return sd

def filter_below_range(data, r):
    sd = []
    for i in data:
        if i['examt'] <= r:
            sd.append(i)
    return sd

def save_data(path, data):
    with open(path, 'w') as f:
        for i in data:
            f.write(i['exname']+' - '+str(i['examt'])+'\n')



while True:
    try:
        path = 'Week_2/Projects/expenses.tt'
        data = fetch_data(path)

        print('-----------------------------------------------------------')
        print('Expense Tracker App')
        print('''-----------------------------------------------------------
        1 - Add expense ( Expense name, amount )
        2 - View all expenses
        3 - Calculate all expenses
        4 - Search expense by name
        5 - Delete expense
        6 - Filter expenses by amount
        7 - Save expenses to file
        0 - Exit
    -----------------------------------------------------------''')
        try:
            c = int(input("Enter your choice (0 - 7) : "))

            if c == 0:
                print('Program terminated successfully!!!')
                break

            elif c == 1:
                name = input("Enter the expense name : ").strip().lower()
                s = search_by_name(name, data)
                if s:
                    print("Expense name already exists!!")
                else:
                    try:
                        amt = float(input("Enter the expense amount : "))
                        ne = add_expense(path, data, name, amt)
                        print(f"Expense Name : {ne[0]} - Expense Amount : {ne[1]}")
                        print("Expense added successfully ✅")
                    except ValueError:
                        print("The amount must be a number or decimal!!!")

            elif c == 2:
                view_data(data)

            elif c == 3:
                view_data(data)
                t = calculate_exps(data)
                print('-------------------------------------------------------')
                print("The total amount of all the expenses is :", t)
                print('-------------------------------------------------------')

            elif c == 4:
                name = input("Enter the expense name you want to search :")
                s = search_by_name(name, data)
                if s:
                    print("The searched expense is :")
                    print(f"Expense name : {s['exname']} - Expense amount : {s['exampt']}")
                else:
                    print("Expense not found !!!")

            elif c == 5:
                name = input("Enter the expense name you want to delete : ").strip().lower()
                s = search_by_name(name, data)
                if s:
                    de = delete_expense(data, name)
                    print("Expense Deleted successfully !!")
                    print("The Expense details are:")
                    print(f"Expense name : {de['exname']} - Expense amount : {de['examt']}")
                else:
                    print("NO expense found with the name : '{name}'")

            elif c == 6:
                print("1. Sort from HIGH to LOW")
                print("2. Sort from LOW to HIGH")
                print("3. Sort the data above given range of amount")
                print("4. Sort the data below given range of amount")
                try:
                    c1 = int(input("Enter your choice for filtering :"))
                    
                    if c1 == 1:
                        sd = filter_data_desc(data)
                        print("Sorted data from High to low")
                        view_data(sd)

                    elif c1 == 2:
                        sd = filter_data_asc(data)
                        print("Sorted data from Low to High")
                        view_data(sd)

                    elif c1 == 3:
                        try:
                            r = float(input("Enter the range of amount :"))
                            print(f"The Expenses with amount greater than or equal to '{r}'")
                            sd = filter_above_range(data, r)
                            view_data(sd)
                        except ValueError:
                            print("The range must be a decimal or integer.")

                    elif c1 == 4:
                        try:
                            r = float(input("Enter the range of amount :"))
                            print(f"The Expenses with amount Less than or equal to '{r}'")
                            sd = filter_below_range(data, r)
                            view_data(sd)
                        except ValueError:
                            print("The range must be a decimal or integer.")

                    else:
                        print('Invalid Choice !!')
                except ValueError:
                    print("The filter choice must be an integer value.")

            elif c == 7:
                if data:
                    save_data(path, data)
                    print("Data saved successfully !!!")
                else:
                    print("No data found to be saved !!")

            else:
                print("Invalid input !! please select between 0 - 7 !!")
        except ValueError:
            print("The choice must be an integer!!")
    except FileNotFoundError:
        print("File not found")
        break