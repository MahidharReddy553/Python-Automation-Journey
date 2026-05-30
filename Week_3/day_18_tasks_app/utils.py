class TaskTitleEmptyError(Exception):
    pass
class TaskStatusError(Exception):
    pass
class TaskPriorityError(Exception):
    pass




def add_data(data, title, desc, priority, status):

    if not status:
        status = "Pending"

    try:
        if title == "":
            raise TaskTitleEmptyError
        if priority not in ("Low", "Medium", "High"):
            raise TaskPriorityError
        if status not in ("Pending", "In Progress", "Completed"):
            raise TaskStatusError
        
        if title != "" and priority in ("Low", "Medium", "High") and status in ("Pending", "In Progress", "Completed"):
            data = data.copy()
            task = {'id': len(data) + 1, 'title': title, 'description': desc, 'priority': priority, 'status': status}
            return task
        else:
            return
        
    except TaskTitleEmptyError:
        print("Task title must not be empty")
    except TaskPriorityError:
        print("Task Priority must be Low/Medium/High")
    except TaskStatusError:
        print("Task status must be Pending/In Progress/Completed")
    except Exception as e:
        print("Some Exception Occured in utils add_data !!!", e)
    

def view_data(data):
    data = data.copy()
    try:
        for task in data:
            print('----------------------------------------------------------------------------------------------------')
            print('Task Id :', task['id'])
            print('Task Title :', task['title'])
            print('Task Description :', task['description'])
            print('Task Priority :', task['priority'])
            print('Task Status :', task['status'])
            print('----------------------------------------------------------------------------------------------------')
    except Exception as e:
        print("Some Exception Occured in utils view_data !!", e)

def search_by_id(data, id):
    data = data.copy()
    found = []
    try:
        for t in data:
            if t.get('id') == id:
                found.append(t)
                break
        return found
            
    except Exception as e:
        print("Some Exception Occured in utils search_by_id !!", e)



def search_by_title(data, title):
    data = data.copy()
    found = []
    try:
        for t in data:
            if t.get('title') == title:
                found.append(t)
        view_data(found)
        return found
    except Exception as e:
        print("Some Exception Occured in utils search_by_title !!", e)


def filter_data_by_status(data, status):
    data = data.copy()
    filtered_data = []
    try:
        for t in data:
            if t.get('status') == status:
                filtered_data.append(t)
        view_data(filtered_data)
        return filtered_data
    except Exception as e:
        print("Some Exception Occured in utils filter_data_by_status!!", e)
    

def filter_data_by_priority(data, priority):
    data = data.copy()
    filtered_data = []
    try:
        for t in data:
            if t.get('priority') == priority:
                filtered_data.append(t)
        view_data(filtered_data)
        return filtered_data
    except Exception as e:
        print("Some Exception Occured in utils filter_data_by_priority !!", e)


def update_status(data, id, status):
    try:
        for t in data:
            if t.get('id') == id:
                t['status'] = status
                print("Task Updated successfully !!!")
                break

    except Exception as e:
                print("Some Exception Occured in utils update_status !!", e)


def update_priority(data, id, priority):
    try:
        for t in data:
            if t.get('id') == id:
                t['priority'] = priority
                print("Task Updated successfully !!!")
                break
        
    except Exception as e:
                print("Some Exception Occured in utils update_priority !!", e)


def delete_by_id(data, id):
    try:
        deleted = []
        for t in data:
            if t.get('id') == id:
                deleted.append(t)
                data.remove(t)
                break
        else:
            print(f"Task with id : {id} not found !!!")
        return deleted
    except Exception as e:
        print("Some Exception Occured in utils delete_by_id !!!", e)


def redefine_ids(data):
    for t in range(len(data)):
        data[t]['id'] = t + 1