#!/usr/bin/python3
"""importing the module to enable write to a file"""
import csv
import requests
import sys


if __name__ == "__main__":
    user_id = sys.argv[1]
    base_url = 'https://jsonplaceholder.typicode.com/'
    users = requests.get(f"{base_url}users/{user_id}").json()
    username = users.get("username")

    todos = requests.get(f"{base_url}todos", params={"userId": user_id}).json()

    # Write to CSV file
    csv_path = f"{user_id}.csv"
    with open(csv_path, 'w', newline="") as csvfile:
        writer = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
        for task in todos:
            writer.writerow([
                user_id,
                username,
                task.get("completed"),
                task.get("title")
            ])
