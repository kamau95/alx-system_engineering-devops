#!/usr/bin/python3
import requests
import sys

#settting the api endpoint
if __name__ == '__main__':
    baseUrl = "https://jsonplaceholder.typicode.com"
    emp_id = sys.argv[1]
    userUrl = f"{baseUrl}/users/{emp_id}"
    user_data = requests.get(userUrl).json()
    employeeName = user_data.get('name')

    todoUrl = f"{baseUrl}/todos?userId={emp_id}"
    tasks = requests.get(todoUrl).json()

    done = 0
    done_tasks = []

    for task in tasks:
        if task.get('completed'):
            done_tasks.append(task)
            done += 1
    print(f"Employee {employeeName} is done with tasks ({done}/{len(tasks)}):")

    for task in done_tasks:
        print(f"\t {task.get('title')}")


