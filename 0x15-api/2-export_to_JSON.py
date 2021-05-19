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

    user_id = argv[1]

    user_dict = req.get('https://jsonplaceholder.typicode.com/users/{}'.
                        format(user_id)).json()
    todo_list = req.get('https://jsonplaceholder.typicode.com/users/{}/todos'.
                        format(user_id)).json()

    username = user_dict['username']
    print_list = []

    for task in todo_list:
        task_info = {}
        task_info['task'] = task['title']
        task_info['completed'] = task['completed']
        task_info['username'] = username
        print_list.append(task_info)

    print_dict = {'{}'.format(user_id): print_list}

    with open("{}.json".format(user_id), 'w') as f:
        json.dump(print_dict, f)
