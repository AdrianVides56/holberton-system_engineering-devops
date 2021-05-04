#!/usr/bin/python3
"""
using this REST API (https://jsonplaceholder.typicode.com),
for a given employee ID, returns information about
his/her TODO list progress.
"""
import requests
from sys import argv


if __name__ == '__main__':
    """Prevent execution of this code when imported"""
    url = 'https://jsonplaceholder.typicode.com/'
    user_id = argv[1]
    completed_tasks, total_tasks = [], 0

    user_name = requests.get(url + 'users/{}'.format(user_id)).json()
    user_tasks = requests.get(url + 'users/{}/todos'.format(user_id)).json()

    for task in user_tasks:
        if task['completed'] is True:
            completed_tasks.append(task)

    total_tasks = len(user_tasks)
    print("Employee {} is done with tasks({}/{}):".format(
        user_name['name'], len(completed_tasks), total_tasks))
    for task in completed_tasks:
        print('\t' + ' {}'.format(task['title']))
