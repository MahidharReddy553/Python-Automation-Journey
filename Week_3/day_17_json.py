import json

data = [
    {"Id": 1, "Name": "Alice", "Marks": 85},
    {"Id": 2, "Name": "Bob", "Marks": 90},
    {"Id": 3, "Name": "Charlie", "Marks": 78},
    {"Id": 4, "Name": "Diana", "Marks": 92},
    {"Id": 5, "Name": "Ethan", "Marks": 88}
]
path = r"D:\Python Automation Journey\Week_3\files\students.json"

def get_data(path):
    with open(path) as file:
        f = json.load(file)
        return f


def add_data(path):
    with open(path, "w") as f:
        json.dump(data, f, indent=4)

def print_data(path):
    with open(path) as jsonfile:
        file = json.load(jsonfile)
        for i in file:
            print('Id :' ,i['Id'], ' - ','Name :', i['Name'], ' - ', 'Marks :', i['Marks'])

def add_student(path, id, name, marks):
    studs = get_data()
    new_s = {'Id':id, 'Name':name, 'Marks':marks}
    studs.append(new_s)
    with open(path, 'a') as jsonfile:
        json.dump(studs, jsonfile, indent=4)

def search_by_name(path, name):
    studs = get_data(path)
    for i in studs:
        if i.get('Name') == name:
            return i
    return


def convert_dict_to_jsonstr(path):
    studs = get_data(path)
    string = json.dumps(studs)
    return string

print(convert_dict_to_jsonstr(path))