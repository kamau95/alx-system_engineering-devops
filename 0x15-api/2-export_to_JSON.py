#!/usr/bin/python3
"""importing the module to enable write to a file"""
import csv
import json
import requests
import sys


if __name__ == "__main__":
    user_id = sys.argv[1]
    base_url = 'https://jsonplaceholder.typicode.com/'
    users = requests.get(f"{base_url}users/{user_id}").json()
    username = users.get("username")

    todos = requests.get(f"{base_url}todos", params={"userId": user_id}).json()

    # Write to CSV file
    json_path = f"{user_id}.json"
    with open(json_path, "w") as jsonfile:
        json.dump({user_id: [{
            "task": t.get("title"),
            "completed": t.get("completed"),
            "username": username
        } for t in todos]}, jsonfile)
