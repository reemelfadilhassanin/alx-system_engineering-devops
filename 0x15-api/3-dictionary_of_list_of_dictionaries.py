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
    u_response = requests.get(base + 'users/')
    if u_response.status_code != 200:
        return print('Error: status_code:', u_response.status_code)
    users = u_response.json()

    u_response = requests.get(base + 'todos/')
    if u_response.status_code != 200:
        return print('Error: status_code:', u_response.status_code)
    todos = u_response.json()

    data = {}
    for user in users:
        user_to = [todo for todo in todos
                   if todo.get('userId') == user.get('id')]
        user_to = [{'username': user.get('username'),
                    'task': todo.get('title'),
                    'completed': todo.get('completed')}
                   for todo in user_to]
        data[str(user.get('id'))] = user_to

    with open('todo_all_employees.json', 'w') as file:
        json.dump(data, file)


if __name__ == '__main__':
    fetch_todo_list_progress()
