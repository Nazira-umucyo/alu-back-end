#!/usr/bin/python3
"""
Script that uses a REST API to return information
about an employee's TODO list progress.
"""

import requests
import sys

if __name__ == "__main__":
        employee_id = int(sys.argv[1])

            # Base URL
                base_url = "https://jsonplaceholder.typicode.com"

                    # Get user info
                        user_url = f"{base_url}/users/{employee_id}"
                            user = requests.get(user_url).json()
                                employee_name = user.get("name")

                                    # Get tasks
                                        todos_url = f"{base_url}/todos?userId={employee_id}"
                                            todos = requests.get(todos_url).json()

                                                # Filter completed tasks
                                                    completed_tasks = [task for task in todos if task.get("completed")]
                                                        num_done = len(completed_tasks)
                                                            total_tasks = len(todos)

                                                                # Print the required output
                                                                    print("Employee {} is done with tasks({}/{}):".format(
                                                                                employee_name, num_done, total_tasks))
                                                                        for task in completed_tasks:
                                                                                    print("\t {}".format(task.get("title")))
