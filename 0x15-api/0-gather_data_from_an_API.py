#!/usr/bin/python3
""" Libraries for making HTTP requests and handling command-line arguments."""
import sys
import requests

# settting the api endpoint
if __name__ == '__main__':
    base_url = "https://jsonplaceholder.typicode.com"
    emp_id = sys.argv[1]
    user_url = f"{base_url}/users/{emp_id}"
    user_data = requests.get(user_url).json()
    employee_name = user_data.get('name')

    todo_url = f"{base_url}/todos?userId={emp_id}"
    tasks = requests.get(todo_url).json()

    done = 0
    done_tasks = []

    for task in tasks:
        if task.get('completed'):
            done_tasks.append(task)
            done += 1
    print(f"Employee {employee_name} is done with tasks \
            ({done}/{len(tasks)}):")

    for task in done_tasks:
        print(f"\t {task.get('title')}")
