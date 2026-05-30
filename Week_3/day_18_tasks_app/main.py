from task_manager import TaskManager


path = r'D:\Python Automation Journey\Week_3\day_18_tasks_app\data\tasks.json'

task_mgr = TaskManager(path)
tasks = task_mgr.load_tasks()

print('---------------------- Task Manager App ----------------------------')

try:
    while True:

        try:
            print('------------------ Menu --------------------')
            print('0. Exit')
            print('1. View all Tasks')
            print('2. Add task')
            print('3. Filter tasks by status')
            print('4. Filter tasks by priority')
            print('5. Search task by id')
            print('6. Update task status')
            print('7. update task priority')
            print('8. Delete task by id')
            print('9. Save all Tasks')
            print('--------------------------------------------')

            saved = False
            choice = input("Enter your choice :")

            if choice == '0':
                if not saved:
                    s = input("Do you want save the data in json file !! (y/n)").lower()
                    if s == 'y':
                        task_mgr.save_all_tasks()
                    else:
                        break
            
            elif choice == "1":
                try:
                    task_mgr.view_all_tasks()
                except Exception as e:
                    print('Some error in choice 1', e)

            elif choice == "2":
                try:
                    title = input("Enter the task title : ")
                    desc = input("Enter the task description : ")
                    priority = input("Enter the priority ('Low'/'Medium'/'High') : ")
                    status = input("Enter the task status ('Pending'/'In Progress'/'Completed') : ")
                    task_mgr.add_task(title, desc, priority, status)
                    print("Task added successfully!!!")
                except Exception as e:
                    print('Some error in choice 2', e)

            elif choice == "3":
                try:
                    task_mgr.filter_by_status()
                except Exception as e:
                    print('Some error in choice 3', e)

            elif choice == "4":
                try:
                    task_mgr.filter_by_priority()
                except Exception as e:
                    print('Some error in choice 4', e)

            elif choice == "5":
                try:
                    id = int(input("Enter the task id you want to search : "))
                    task_mgr.search_task_by_id(id)
                except ValueError:
                    print("The id must be an integer")
                except Exception as e:
                    print("Some exception occured in choice 5!!", e)

            elif choice == "6":
                try:
                    id = int(input("Enter the id of the task to update status : "))
                    task_mgr.update_task_status(id)
                except ValueError:
                    print('The id must be an integer !!')
                except Exception as e:
                    print("Some exception occured in choice 6!!", e)


            elif choice == "7":
                try:
                    id = int(input("Enter the id of the task to update priority : "))
                    task_mgr.update_task_priority(id)
                except ValueError:
                    print('The id must be an integer !!')
                except Exception as e:
                    print("Some exception occured in choice 7!!", e)

            elif choice == "8":
                try:
                    id = int(input("Enter the id of the task you want to delete : "))
                    task_mgr.delete_task_by_id(id)
                except ValueError:
                    print('The id must be an integer !!')
                except Exception as e:
                    print("Some exception occured in choice 8!!", e)

            elif choice == "9":
                try:
                    task_mgr.save_all_tasks()
                except Exception as e:
                    print('Some error in choice 9', e)


        except Exception as e:
            print("Some error occured inside main while loop !!!", e)


except Exception as e:
    print("Some exception occured in main while loop !!!")
