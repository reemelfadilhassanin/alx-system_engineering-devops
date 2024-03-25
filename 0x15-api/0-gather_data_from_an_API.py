#!/usr/bin/python3
"""
apython script using this REST API, for a given employee ID,
returns information about his/her TODO list progress
"""
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

    user_to = [to for to in userdos
               if to.get('userId') == user_d.get('id')]
    completed = [to for to in user_to if to.get('completed')]
    print('Employee', user_d.get('name'),
          'is done with tasks({}/{}):'.
          format(len(completed), len(user_to)))
    [print('\t', to.get('title')) for to in completed]


if __name__ == '__main__':
    fetch_todo_list_progress()
