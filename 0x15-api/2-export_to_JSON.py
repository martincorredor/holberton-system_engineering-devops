#!/usr/bin/python3
"""export data in the JSON format. """
import json
import requests
from sys import argv


if __name__ == '__main__':
    users = requests.get("http://jsonplaceholder.typicode.com/users")
    for user in users.json():
        if user.get('id') == int(argv[1]):
            USERNAME = (user.get('username'))
            break
    TASK_TITLE = []
    todos = requests.get("http://jsonplaceholder.typicode.com/todos")
    for todo in todos.json():
        if todo.get('userId') == int(argv[1]):
            TASK_TITLE.append((todo.get('completed'), todo.get('title')))

    todo = []
    for task in TASK_TITLE:
        todo.append({"task": task[1], "completed": task[0],
                     "username": USERNAME})
    data = {str(argv[1]): todo}
    filename = "{}.json".format(argv[1])
    with open(filename, "w") as f:
        json.dump(data, f)
