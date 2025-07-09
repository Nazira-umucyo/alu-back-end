#!/usr/bin/python3
"""
Using a REST API and a given employee ID,
return information about their TODO list.
"""

import requests
import sys

if __name__ == "__main__":
    employee_id = int(sys.argv[1])
    url = "https://jsonplaceholder.typicode.com"

    # Get user info
    user = requests.get("{}/users/{}".format(url, employee_id)).json()
    employee_name = user.get("name")

    # Get todos
    todos = requests.get("{}/todos?userId={}".format(url, employee_id)).json()
    completed_tasks = [task for task in todos if task.get("completed")]

    # Print the result
    print("Employee {} is done with tasks({}/{}):".format(
        employee_name, len(completed_tasks), len(todos)))

    for task in completed_tasks:
        print("\t {}".format(task.get("title")))
