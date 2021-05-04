#!/usr/bin/python3
"""
Using this REST API (https://jsonplaceholder.typicode.com/),
for a given employee ID, returns information about his/her TODO list progress.
"""
import requests
from sys import argv


if __name__ == '__main__':
    users = requests.get("https://jsonplaceholder.typicode.com/users")
    todos = requests.get("http://jsonplaceholder.typicode.com/todos")
    for user in users.json():
        if user.get('id') == int(argv[1]):
            EMPLOYEE_NAME = (user.get('name'))
            break
    TOTAL_NUM_OF_TASKS = 0
    NUMBER_OF_DONE_TASKS = 0
    TASK_TITLE = []

    for todo in todos.json():
        if todo.get('userId') == int(argv[1]):
            TOTAL_NUM_OF_TASKS += 1
            if todo.get('completed'):
                NUMBER_OF_DONE_TASKS += 1
                TASK_TITLE.append(todo.get('title'))

    print("Employee {} is done with tasks({}/{}):".format(EMPLOYEE_NAME,
                                                          NUMBER_OF_DONE_TASKS,
                                                          TOTAL_NUM_OF_TASKS))
    for task in TASK_TITLE:
        print("\t {}".format(task))
