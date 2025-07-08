#!/usr/bin/python3
"""
0-gather_data_from_an_API.py
"""

import requests
import sys

if len(sys.argv) != 2:
        print(f"Usage: {sys.argv[0]} <employee_id>")
            sys.exit(1)

            try:
                    employee_id = int(sys.argv[1])
            except ValueError:
                    print("Employee ID must be an integer")
                        sys.exit(1)

                        base_url = "https://jsonplaceholder.typicode.com"

                        user_response = requests.get(f"{base_url}/users/{employee_id}")
                        if user_response.status_code != 200:
                                print("Employee not found")
                                    sys.exit(1)
                                    user_data = user_response.json()
                                    employee_name = user_data.get("name", "").strip()

                                    todos_response = requests.get(f"{base_url}/todos", params={"userId": employee_id})
                                    if todos_response.status_code != 200:
                                            print("Failed to retrieve TODO list")
                                                sys.exit(1)
                                                todos = todos_response.json()

                                                total_tasks = len(todos)
                                                done_tasks = [task for task in todos if task.get("completed") is True]
                                                number_done = len(done_tasks)

                                                print(f"Employee {employee_name} is done with tasks({number_done}/{total_tasks}):")
                                                for task in done_tasks:
                                                        title = task.get("title", "").strip()
                                                            print(f"\t {title}")
