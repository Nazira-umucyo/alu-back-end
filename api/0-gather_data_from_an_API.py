#!/usr/bin/python3
"""
0-gather_data_from_an_API.py
Fetch employee TODO list progress from a REST API.
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

                        # Get employee data
                        user_response = requests.get("{}/users/{}".format(base_url, employee_id))
                        if user_response.status_code != 200:
                                print("Employee not found")
                                    sys.exit(1)

                                    user_data = user_response.json()
                                    employee_name = user_data.get("name", "").strip()

                                    # Get TODOs
                                    todos_response = requests.get("{}/todos".format(base_url), params={"userId": employee_id})
                                    if todos_response.status_code != 200:
                                            print("Failed to retrieve TODO list")
                                                sys.exit(1)

                                                todos = todos_response.json()

                                                total_tasks = len(todos)
                                                done_tasks = [task for task in todos if task.get("completed") is True]
                                                number_done = len(done_tasks)

                                                # ✅ Print first line with correct spacing
                                                print("Employee {} is done with tasks({}/{}):".format(employee_name, number_done, total_tasks))

                                                # ✅ Print tasks, formatted correctly
                                                for task in done_tasks:
                                                        print("\t {}".format(task.get("title", "").strip()))
