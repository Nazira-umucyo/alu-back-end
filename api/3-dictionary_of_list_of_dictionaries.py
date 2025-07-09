#!/usr/bin/python3
"""
Exports all employees' TODO lists to a JSON file.
"""

import json
import requests

if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com"

    # Fetch all users
    users = requests.get(f"{url}/users").json()

    all_tasks = {}

    for user in users:
        user_id = user.get("id")
        username = user.get("username")
        todos = requests.get(f"{url}/todos?userId={user_id}").json()

        task_list = []
        for task in todos:
            task_list.append({
                "username": username,
                "task": task.get("title"),
                "completed": task.get("completed")
            })

        all_tasks[str(user_id)] = task_list

    # Write to JSON file
    with open("todo_all_employees.json", "w") as json_file:
        json.dump(all_tasks, json_file)
