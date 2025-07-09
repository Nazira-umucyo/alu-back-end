#!/usr/bin/python3
"""
Exports an employee's TODO list data to a CSV file.
"""

import csv
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

    # Open CSV file for writing
    filename = "{}.csv".format(employee_id)
    with open(filename, "w", newline='') as csvfile:
        writer = csv.writer(csvfile, quoting=csv.QUOTE_ALL)

        for task in todos:
            writer.writerow([
                employee_id,
                username,
                task.get("completed"),
                task.get("title")
            ])
