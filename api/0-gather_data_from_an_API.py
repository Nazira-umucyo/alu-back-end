#!/usr/bin/python3
"""
0-gather_data_from_an_API.py
Fetch employee TODO list progress from JSONPlaceholder API.
"""

import requests
import sys


if len(sys.argv) != 2:
        print("Usage: {} <employee_id>".format(sys.argv[0]))
            sys.exit(1)

            try:
                    employee_id = int(sys.argv[1])
            except ValueError:
                    print("Employee ID must be an integer")
                        sys.exit(1)

                        base_url = "https://jsonplaceholder.typicode.com"

                        # Get user information
                        user_url = "{}/users/{}".format(base_url, employee_id)
                        user_response = requests.get(user_url)
                        if user_response.status_code != 200:
                                print("User not found")
                                    sys.exit(1)

                                    user_data = user_response.json()
                                    employee_name = user_data.get("name", "").strip()

                                    # Get todos
                                    todos_url = "{}/todos".format(base_url)
                                    todos_response = requests.get(todos_url, params={"userId": employee_id})
                                    if todos_response.status_code != 200:
                                            print("Failed to fetch tasks")
                                                sys.exit(1)

                                                todos = todos_response.json()

                                                # Count completed tasks
                                                total_tasks = len(todos)
                                                done_tasks = [task for task in todos if task.get("completed") is True]
                                                done_count = len(done_tasks)

                                                # Print result
                                                print("Employee {} is done with tasks({}/{}):".format(
                                                        employee_name, done_count, total_tasks))

                                                for task in done_tasks:
                                                        title = task.get("title", "").strip()
                                                            print("\t {}".format(title))
