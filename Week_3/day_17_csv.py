import csv

path = r"D:\Python Automation Journey\Week_3\files\students.csv"

def create_data(path):
    with open(path, 'w', newline='') as csvfile:
        fieldnames = ['Id', 'Name', 'Marks']
        file = csv.DictWriter(csvfile, fieldnames=fieldnames)
        file.writeheader()
        file.writerow({'Id': 1, 'Name': 'Alice', 'Marks': 85})
        file.writerow({'Id': 2, 'Name': 'Bob', 'Marks': 90})
        file.writerow({'Id': 3, 'Name': 'Charlie', 'Marks': 78})
        file.writerow({'Id': 4, 'Name': 'Diana', 'Marks': 92})
        file.writerow({'Id': 5, 'Name': 'Ethan', 'Marks': 88})


def calculate_avg(path):
    with open(path) as csvfile:
        file = csv.DictReader(csvfile)
        data = tuple(file)
        s = sum(int(i['Marks']) for i in data)
        n = len(data)
        avg = s / n
        return round(avg, 2)


def add_new_stud(path,id, name , marks):
    with open(path, 'a', newline='') as csvfile:
        fieldnames = ['Id', 'Name', 'Marks']
        file = csv.DictWriter(csvfile, fieldnames = fieldnames)
        file.writerow({'Id':id, 'Name':name, 'Marks':marks})

def print_studs(path):
    with open(path, newline='') as csvfile:
        file = csv.reader(csvfile)
        for i in list(file)[1:]:
            print('Name :', i[1], ' - ', 'Marks :', i[2])


def search_by_name(path, name):
    with open(path, newline='') as csvfile:
        file = csv.DictReader(csvfile)
        for i in file:
            if i.get('Name') == name:
                return i
        return
    

print(search_by_name(path, 'pb'))