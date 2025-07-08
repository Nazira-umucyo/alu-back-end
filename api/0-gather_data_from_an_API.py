#!/usr/bin/python3
"""
Fetches and displays an employee's TODO list progress using a REST API.
"""

import requests
import sys

if __name__ == "__main__":
    employee_id = int(sys.argv[1])
    base_url = "https://jsonplaceholder.typicode.com"

    # Fetch user info
    user = requests.get("{}/users/{}".format(base_url, employee_id)).json()
    employee_name = user.get("name")

    # Fetch todos
    todos = requests.get("{}/todos?userId={}".format(base_url, employee_id)).json()
    total_tasks = len(todos)
    completed_tasks = [task for task in todos if task.get("completed")]

    # Output
    print("Employee {} is done with tasks({}/{}):".format(
        employee_name, len(completed_tasks), total_tasks))

    for task in completed_tasks:
        print("\t {}".format(task.get("title")))
