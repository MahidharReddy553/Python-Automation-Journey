from file_handler import *
from utils import *

class TaskManager:
    
    def __init__(self, path):
        self.path = path
        self.__data = get_data(path)

    def load_tasks(self):
        return self.__data

    def save_all_tasks(self):
        # for t in range(len(self.__data)):
        #     self.__data[t]['id'] = t + 1
        save_data(self.path, self.__data)


    def view_all_tasks(self):
        print('------------------------------------------ All Tasks -------------------------------------------------')
        view_data(self.__data)


    def add_task(self, title, desc, priority, status = None):
        t = add_data(self.__data, title, desc, priority, status)
        if t:
            self.__data.append(t)

    def filter_by_status(self):
        print("Select the status choice to filter")
        print('1. Pending')
        print('2. In Progress')
        print('3. Completed')
        try:
            choice = input("Enter your choice(1/2/3) : ")
            if choice == "1":
                filter_data_by_status(self.__data, 'Pending')
            elif choice == "2":
                filter_data_by_status(self.__data, 'In Progress')
            elif choice == "3":
                filter_data_by_status(self.__data, 'Completed')
            else:
                print("Invalid Choice !!!. Select choice among 1/2/3")
        except Exception as e:
            print("Some Exception Occured !!", e)


    def filter_by_priority(self):
        data = self.load_tasks()
        print("Select the priority choice to filter")
        print('1. Low')
        print('2. Medium')
        print('3. High')
        try:
            choice = input("Enter your choice(1/2/3) : ")
            if choice == "1":
                filter_data_by_priority(data, 'Low')
            elif choice == "2":
                filter_data_by_priority(data, 'Medium')
            elif choice == "3":
                filter_data_by_priority(data, 'High')
            else:
                print("Invalid Choice !!!. Select choice among 1/2/3")
        except Exception as e:
            print("Some Exception Occured !!", e)

    def search_task_by_id(self, id):
        f = search_by_id(self.__data, id)
        if f:
            print(f'Task with id : {id} found')
            view_data(f)
        else:
            print(f'Task with id : {id} not found')


    def update_task_status(self, id):
        try:
          t = search_by_id(self.__data, id)
          if t:
            print(f"Select the status choice to update task with id : {id}")
            print('1. Pending')
            print('2. In Progress')
            print('3. Completed')
            choice = input("Enter your choice(1/2/3) : ")
            if choice == "1":
                update_status(self.__data, id, 'Pending')
            elif choice == "2":
                update_status(self.__data, id, 'In Progress')
            elif choice == "3":
                update_status(self.__data, id, 'Completed')
            else:
                print("Invalid Choice !!!. Select choice among 1/2/3")
          else:
              print(f"Task with id : {id} not found")  

        except Exception as e:
            print("Some Exception Occured !!", e)
              


    def update_task_priority(self, id):
        try:
          t = search_by_id(self.__data, id)
          if t:
            print(f"Select the priority choice to update task with id : {id}")
            print('1. Low')
            print('2. Medium')
            print('3. High')
            choice = input("Enter your choice(1/2/3) : ")
            if choice == "1":
                update_status(self.__data, id, 'Low')
            elif choice == "2":
                update_status(self.__data, id, 'Medium')
            elif choice == "3":
                update_status(self.__data, id, 'High')
            else:
                print("Invalid Choice !!!. Select choice among 1/2/3")
          else:
              print(f"Task with id : {id} not found")  

        except Exception as e:
            print("Some Exception Occured !!", e)
        

    def delete_task_by_id(self, id):
        de = delete_by_id(self.__data, id)
        if de:
            print("---------- deleted task -----------")
            view_data(de)
            redefine_ids(self.__data)



    
if __name__ == '__main__':
    tm = TaskManager(r'Week_3\day_18_tasks_app\data\tasks.json')
    # tm.view_all_tasks()
    # tm.save_all_tasks()
    # print(tm.load_tasks())
    # tm.filter_by_status()
    # tm.filter_by_priority()
    tm.delete_task_by_id(5)

    tm.save_all_tasks()
