#!/usr/bin/python3
"""
apython script using this REST API, for a given employee ID,
returns information about his/her TODO list progress
"""
import json
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
    user = u_response.json()

    u_response = requests.get(base + 'todos/')
    if u_response.status_code != 200:
        return print('Error: status_code:', u_response.status_code)
    todos = u_response.json()
    user_to = [todo for todo in todos
               if todo.get('userId') == user.get('id')]
    completed = [todo for todo in user_to if todo.get('completed')]

    user_to = [{'task': todo.get('title'),
                'completed': todo.get('completed'),
                'username': user.get('username')}
               for todo in user_to]
    data_user = {eid: user_to}
    with open(eid + '.json', 'w') as file:
        json.dump(data_user, file)


if __name__ == '__main__':
    fetch_todo_list_progress()
