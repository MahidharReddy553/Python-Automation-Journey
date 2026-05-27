import requests

def fetch_all(url):
    response = requests.get(url)
    if response.status_code == 200:    
        return response.json()
    else:
        return


def fetch_user_by_id(id):
    url = f"https://jsonplaceholder.typicode.com/users/{id}"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        return
    
def view_user(data):
    print('--------------------------- User Details ---------------------------')
    print('User id :', data.get('id'))
    print('Name :', data.get('name'))
    print('Username :', data.get('username'))
    print('email :', data.get('email'))
    print('Address :', data.get('address'))
    print('Phone :', data.get('phone'))
    print('Website :', data.get('website'))
    print('Company :', data.get('company'))
    print('----------------------------------------------------------------------')

def view_data(data):
    print('------------------------------------------------ All Users -----------------------------------------')
    for i in data:
        print('-----------------------------------------------------------------------------------------------')
        print('User id :', i.get('id'))
        print('Name :', i.get('name'))
        print('Username :', i.get('username'))
        print('email :', i.get('email'))
        print('Address :', i.get('address'))
        print('Phone :', i.get('phone'))
        print('Website :', i.get('website'))
        print('Company :', i.get('company'))
        print('-----------------------------------------------------------------------------------------------')




while True:
    url = "https://jsonplaceholder.typicode.com/users"
    print('1. Fetch all users')
    print('2. Fetch user by id')
    print('3. Exit')
    try:
        c = int(input("Enter your choice(1/2/3) : "))

        if c == 1:
            data = fetch_all(url)
            view_data(data)

        elif c == 2:
            try:
                id = input("Enter the user id: ")
                data = fetch_user_by_id(id)
                view_user(data)
            except Exception:
                print(Exception, 'Occured')

        elif c == 3:
            break

        else:
            print('Invalid Choice please select between (1/2/3)')
    except Exception:
        print(Exception, "Occured")