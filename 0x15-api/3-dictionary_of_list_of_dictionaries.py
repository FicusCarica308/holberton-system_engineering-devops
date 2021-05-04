#!/usr/bin/python3
"""
Description:
    A Python script that, using this REST API
(https://intranet.hbtn.io/rltoken/0Ltm_dXy-m4E9jchBrKLVA),
for a given employee ID, returns information about
his/her TODO list progress.

Also exports data in the JSON format...
"""
if __name__ == "__main__":
    import requests as req
    from sys import argv
    import json

    user_dict = req.get('https://jsonplaceholder.typicode.com/users').json()
    print_dict = {}

    for user in user_dict:
        user_id = user['id']
        url = 'https://jsonplaceholder.typicode.com/users/{}/todos'
        todo_list = req.get(url.format(user_id)).json()
        username = user['username']

        print_list = []

        for task in todo_list:
            task_info = {}
            task_info['task'] = task['title']
            task_info['completed'] = task['completed']
            task_info['username'] = username
            print_list.append(task_info)
        print_dict['{}'.format(user_id)] = print_list

    with open("todo_all_employees.json", 'w') as f:
        json.dump(print_dict, f)
