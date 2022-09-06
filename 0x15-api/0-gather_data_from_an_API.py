#!/usr/bin/python3
"""
https://jsonplaceholder.typicode.com/
For a given employee ID, returns information about his/her TODO list progress.
"""

import requests
from sys import argv

if __name__ == '__main__':
    """
    Display on the standard output the employee TODO list progress.
    """
    
    TOTAL_NUMBER_OF_TASKS = 0
    NUMBER_OF_DONE_TASKS = 0
    TASK_TITLE = 0
    
    id = argv[1]
    
    users = requests.get("https://jsonplaceholder.typicode.com/users")
    
    for user in users.json():
        if user.get('id') == id:
            EMPLOYEE_NAME = user.get('name')
            break
            
    todos = requests.get("https://jsonplaceholder.typicode.com/todos")
    
    for task in todos.json():
        if task.get("userId") == id:
            TOTAL_NUMBER_OF_TASKS += 1
            if task.get("completed") == True:
                NUMBER_OF_DONE_TASKS += 1