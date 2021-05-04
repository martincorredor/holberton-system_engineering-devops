#!/usr/bin/python3
"""
Export data in the CSV format.
"""
import csv
import requests
from sys import argv


if __name__ == '__main__':

    users = requests.get("http://jsonplaceholder.typicode.com/users")
    todos = requests.get("http://jsonplaceholder.typicode.com/todos")
    for user in users.json():
        if user.get('id') == int(argv[1]):
            USERNAME = (user.get('username'))
            break
    TASK_TITLE = []
    for todo in todos.json():
        if todo.get('userId') == int(argv[1]):
            TASK_TITLE.append((todo.get('completed'), todo.get('title')))

    file_name = "{}.csv".format(argv[1])
    with open(file_name, "w") as csvfile:
        fieldnames = ["USER_ID", "USERNAME",
                      "TASK_COMPLETED_STATUS", "TASK_TITLE"]
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames,
                                quoting=csv.QUOTE_ALL)
        for task in TASK_TITLE:
            writer.writerow({"USER_ID": argv[1], "USERNAME": USERNAME,
                             "TASK_COMPLETED_STATUS": task[0],
                             "TASK_TITLE": task[1]})
