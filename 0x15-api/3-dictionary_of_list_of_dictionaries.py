#!/usr/bin/python3
"""
https://jsonplaceholder.typicode.com/
Using what you did in the task #0, extend your Python script
to export data in the JSON format.
"""

import json
import requests
from sys import argv

if __name__ == '__main__':
    """
    Display on the standard output the employee TODO list progress.
    """

    USER_ID = 0

    users = requests.get("https://jsonplaceholder.typicode.com/users")
    todos = requests.get("https://jsonplaceholder.typicode.com/todos")
    
    todolist = []
    tododict = {}
    for user in users.json():
        USER_ID = user.get("id")
        USERNAME = user.get("username")
        with open("todo_all_employees.json", "w", encoding="utf-8") as file:
            for task in todos.json():
                dict = {}
                if user.get("id") == id:
                    dict['task'] = task['title']
                    dict['completed'] = task['completed']
                    dict['username'] = USERNAME
                    todolist.append(dict)
            tododict[id] = todolist
            file.write(json.dumps(tododict))
