#!/usr/bin/python3
"""
https://jsonplaceholder.typicode.com/
Using what you did in the task #0, extend your Python script to export data in the JSON format.    
"""

import json
import requests
from sys import argv

if __name__ == '__main__':
    """
    Display on the standard output the employee TODO list progress.
    """

    USER_ID  = 0
    TASK_TITLE = []
    
    #id must be int
    id = int(argv[1])
    
    users = requests.get("https://jsonplaceholder.typicode.com/users")
    
    for user in users.json():
        if user.get("id") == id:
            USER_ID = user.get("id")
            USERNAME = user.get("username")
            break
            
    todos = requests.get("https://jsonplaceholder.typicode.com/todos")
    
    dict = {}
        
        
    
    file_name = "{}.json".format(USER_ID)
    with open(file_name, "w", encoding = 'utf-8') as file:
        json.dump()