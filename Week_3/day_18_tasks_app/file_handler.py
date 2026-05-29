import json

def get_data(path):
    try:
        with open(path) as file:
            tasks = json.load(file)
            return tasks
    except Exception as e:
        print("Some Exception Occured !!", e)


def save_data(path, data):
    try:
        with open(path, 'w') as file:
            json.dump(data, file, indent=4)

        print("Data saved successfully !!")

    except Exception as e:
        print("Some Exception Occured !!", e)