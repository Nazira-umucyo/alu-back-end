#!/usr/bin/python3
"""
Exports an employee's TODO list data to a JSON file.
"""

import json
import requests
import sys

if __name__ == "__main__":
    employee_id = int(sys.argv[1])
    url = "https://jsonplaceholder.typicode.com"

    # Get user info
    user = requests.get("{}/users/{}".format(url, employee_id)).json()
    username = user.get("username")

    # Get all todos
    todos = requests.get("{}/todos?userId={}".format(url, employee_id)).json()

    # Build the JSON data
    tasks = []
    for task in todos:
        tasks.append({
            "task": task.get("title"),
            "completed": task.get("completed"),
            "username": username
        })

    data = {str(employee_id): tasks}

    # Write to file
    with open("{}.json".format(employee_id), "w") as jsonfile:
        json.dump(data, jsonfile)
