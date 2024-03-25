#!/usr/bin/python3
"""
apython script using this REST API, for a given employee ID,
returns information about his/her TODO list progress
"""
import json
import requests
import sys

base_url = 'https://jsonplaceholder.typicode.com/'


def fetch_todo_list_progress():
    '''Fetches TODO list progress'''
    if not len(sys.argv):
        return print('USAGE:', __file__, '<employee id>')
    eid = sys.argv[1]
    try:
        _eid = int(sys.argv[1])
    except ValueError:
        return print('Employee id must be an integer')

    response = requests.get(base_url + 'users/' + eid)
    if response.status_code == 404:
        return print('User id not found')
    elif response.status_code != 200:
        return print('Error: status_code:', response.status_code)
    user = response.json()

    response = requests.get(base_url + 'todos/')
    if response.status_code != 200:
        return print('Error: status_code:', response.status_code)
    todos = response.json()
    user_todos = [todo for todo in todos
                  if todo.get('userId') == user.get('id')]
    json_data = {user.get('id'): [{"task": todo.get('title'), "completed": todo.get(
        'completed'), "username": user.get('name')} for todo in user_todos]}

    # Export to JSON
    with open(f"{eid}.json", 'w') as jsonfile:
        json.dump(json_data, jsonfile, indent=4)

    print(f"Data exported to {eid}.json")


if __name__ == '__main__':
    fetch_todo_list_progress()
