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
    if not len(sys.argv):
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
    user_to = [to for to in todos
               if to.get('userId') == user.get('id')]
    completed = [to for to in user_to if to.get('completed')]

    with open(eid + '.csv', 'w') as csvfile:
        writer_csv = csv.writer(csvfile, lineterminator='\n',
                                quoting=csv.QUOTE_ALL)
        [writer_csv.writerow(['{}'.format(field) for field in
                              (to.get('userId'), user.get('username'),
                               to.get('completed'), to.get('title'))])
         for to in user_to]


if __name__ == '__main__':
    fetch_todo_list_progress()
