
def add_data(data, title, desc, priority, status = "pending"):
    pass

def view_data(data):
    print('------------------------------------------ All Tasks -------------------------------------------------')
    for task in data:
        print('----------------------------------------------------------------------------------------------------')
        print('Task Id :', task['id'])
        print('Task Title :', task['title'])
        print('Task Description :', task['description'])
        print('Task Priority :', task['priority'])
        print('Task Status :', task['status'])
        print('----------------------------------------------------------------------------------------------------')


def search_by_id(data):
    pass

def search_by_title(data):
    pass

def filter_by_status(data):
    pass

def filter_by_priority(data):
    pass
