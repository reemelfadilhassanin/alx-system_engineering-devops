#!/usr/bin/python3
"""
A Python script using this REST API, for a given employee ID,
returns information about his/her TODO list progress
"""
import csv
import requests
import sys

base = 'https://jsonplaceholder.typicode.com/'


def fetch_todo_list_progress():
    '''this defines to fetch list progress'''
    if len(sys.argv) < 2:
        return print('USAGE:', __file__, '<employee id>')
    eid = sys.argv[1]
    try:
        _eid = int(sys.argv[1])
    except ValueError:
        return print('Employee id must be an integer')

    u_response = requests.get(base + 'users/' + eid)
    if u_response.status_code == 404:
        return print('User id not found')
    elif u_response.status_code != 200:
        return print('Error: status_code:', u_response.status_code)
    user_d = u_response.json()

    u_response = requests.get(base + 'todos/')
    if u_response.status_code != 200:
        return print('Error: status_code:', u_response.status_code)
    userdos = u_response.json()

    user_todos = [todo for todo in userdos
                  if todo.get('userId') == user_d.get('id')]

    # Export to CSV
    csv_file = f"{user_d.get('id')}.csv"
    with open(csv_file, mode='w', newline='') as file:
        writer = csv.writer(file, quoting=csv.QUOTE_ALL)
        writer.writerow(
            ["USER_ID", "USERNAME", "TASK_COMPLETED_STATUS", "TASK_TITLE"])
        for todo in user_todos:
            writer.writerow([todo.get('userId'), user_d.get(
                'name'), todo.get('completed'), todo.get('title')])

    print(f"Data exported to {csv_file}")


if __name__ == '__main__':
    fetch_todo_list_progress()
