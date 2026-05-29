from file_handler import *
from utils import *

class TaskManager:
    
    def __init__(self, path):
        self.path = path
        self.data = get_data(path)


    def save_all_tasks(self):
        save_data(self.path, self.data)


    def view_all_tasks(self):
        view_data(self.data)


        

    
if __name__ == '__main__':
    tm = TaskManager(r'D:\Python Automation Journey\Week_3\day_18_tasks_app\data\tasks.json')
    tm.view_all_tasks()
    tm.save_all_tasks()
