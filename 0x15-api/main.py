#!/usr/bin/python3
#modules needed
import requests
import sys


base_url = "https://jsonplaceholder.typicode.com/todos"
employee_number = sys.argv[1]  # Example employee number
url = f"{base_url}/{employee_number}"

#make request
response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    print(data)
else:
    print("failed to retrieve data", response.status_code)
