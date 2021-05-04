#!/usr/bin/python3
"""export data in the JSON format."""
import json
import requests


if __name__ == '__main__':

    users = requests.get("http://jsonplaceholder.typicode.com/users")
    USERS_ = []
    for user in users.json():
        USERS_.append((user.get('id'), user.get('username')))
    TASK_STATUS_TITLE = []
    todos = requests.get("http://jsonplaceholder.typicode.com/todos")
    for todo in todos.json():
        TASK_STATUS_TITLE.append((todo.get('userId'),
                                  todo.get('completed'),
                                  todo.get('title')))

    data = dict()
    for user in USERS_:
        todo = []
        for task in TASK_STATUS_TITLE:
            if task[0] == user[0]:
                todo.append({"task": task[2], "completed": task[1],
                            "username": user[1]})
        data[str(user[0])] = todo
    filename = "todo_all_employees.json"
    with open(filename, "w") as f:
        json.dump(data, f, sort_keys=True)
