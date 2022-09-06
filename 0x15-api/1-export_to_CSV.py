#!/usr/bin/python3
"""
https://jsonplaceholder.typicode.com/
Using what you did in the task #0, extend your Python script to export data in the CSV format.    
"""

import csv
import requests
from sys import argv

if __name__ == '__main__':
    """
    Display on the standard output the employee TODO list progress.
    """

    USER_ID  = 0
    USERNAME = ""
    TAS_COMPLETED_STATUS = False
    TASK_TITLE = ""
    
    #id must be int
    id = int(argv[1])
    
    users = requests.get("https://jsonplaceholder.typicode.com/users")
    
    for user in users.json():
        if user.get("id") == id:
            USER_ID = user.get("id")
            USERNAME = user.get("username")
            break
            
    todos = requests.get("https://jsonplaceholder.typicode.com/todos")
    
    file_name = "{}.csv".format(USER_ID)
    with open(file_name, "w", encoding = 'utf-8') as file:
        for task in todos.json():
            if task.get("userId") == id:
                TASK_TITLE = task.get("title")
                if task.get("completed") == True:
                    TASK_COMPLETED_STATUS = True
                else:
                    TASK_COMPLETED_STATUS = False
                
                file.write('"{}","{}","{}","{}"\n'.format(USER_ID, USERNAME, TASK_COMPLETED_STATUS, TASK_TITLE))

