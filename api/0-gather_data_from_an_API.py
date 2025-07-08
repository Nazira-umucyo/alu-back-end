#!/usr/bin/python3
"""Fetches and displays an employee's TODO list progress from an API."""

import requests
import sys

if len(sys.argv) != 2:
        sys.exit(1)

        try:
                employee_id = int(sys.argv[1])
        except ValueError:
                sys.exit(1)

                base_url = "https://jsonplaceholder.typicode.com"

                # Fetch user data
                user_url = f"{base_url}/users/{employee_id}"
                user_response = requests.get(user_url)
                user_data = user_response.json()
                employee_name = user_data.get("name", "").strip()

                # Fetch tasks
                todos_url = f"{base_url}/todos"
                todos_response = requests.get(todos_url, params={"userId": employee_id})
                todos = todos_response.json()

                # Process tasks
                total_tasks = len(todos)
                done_tasks = [task for task in todos if task.get("completed")]
                done_count = len(done_tasks)

                # Output
                print("Employee {} is done with tasks({}/{}):".format(
                        employee_name, done_count, total_tasks))
                for task in done_tasks:
                        print("\t {}".format(task.get("title", "").strip()))
