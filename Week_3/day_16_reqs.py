import requests

url = "https://jsonplaceholder.typicode.com/users"

response = requests.get(url)
data = response.json()
st_code = response.status_code

print(data)
print(st_code)

for user in data:
    print('name :', user['name'],' - ',  'email :',  user['email'])


user1 = requests.get("https://jsonplaceholder.typicode.com/users/1")
print(user1.json())