#!/usr/bin/python3
"""
Using a REST API and a given employee ID,
return information about their TODO list.
"""

import sys
import requests

if __name__ == "__main__":
    employee_id = int(sys.argv[1])
    base_url = "https://jsonplaceholder.typicode.com"

    # Get employee information
    user = requests.get(f"{base_url}/users/{employee_id}").json()
    employee_name = user.get("name")

    # Get todos
    todos = requests.get(f"{base_url}/todos?userId={employee_id}").json()
    total_tasks = len(todos)
    completed_tasks = [task for task in todos if task.get("completed")]

    # Print required output
    print("Employee {} is done with tasks({}/{}):".format(
        employee_name, len(completed_tasks), total_tasks))

    for task in completed_tasks:
        print("\t {}".format(task.get("title")))
