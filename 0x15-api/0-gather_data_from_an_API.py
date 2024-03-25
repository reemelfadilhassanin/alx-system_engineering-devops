#!/usr/bin/python3
"""
apython script using this REST API, for a given employee ID,
returns information about his/her TODO list progress
"""
import requests
import sys


def fetch_todo_list(employee_id):
    base = "https://jsonplaceholder.typicode.com"
    user_url = f"{base}/users/{employee_id}"
    todos = f"{base}/todos?userId={employee_id}"
    user_response = requests.get(user_url)
    if user_response.status_code != 200:
        print("Error fetching user info")
        return

    user_data = user_response.json()
    employee_name = user_data['name']
    todos_response = requests.get(todos)
    if todos_response.status_code != 200:
        print("Error fetching TODO list")
        return

    todos_data = todos_response.json()
    total_tasks = len(todos_data)
    done_tasks = [todo['title'] for todo in todos_data if todo['completed']]

    print(
        f"Employee {employee_name} is done with tasks({len(done_tasks)}/{total_tasks}):")
    for task in done_tasks:
        print(f"\t{task}")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <employee_id>")
        sys.exit(1)

    employee_id = int(sys.argv[1])
    fetch_todo_list(employee_id)
