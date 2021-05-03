#!/usr/bin/python3
"""
Description:
    A Python script that, using this REST API
(https://intranet.hbtn.io/rltoken/0Ltm_dXy-m4E9jchBrKLVA),
for a given employee ID, returns information about
his/her TODO list progress.

Also exports data in the CSV format...
"""
if __name__ == "__main__":
    import requests as req
    from sys import argv
    import csv

    user_id = argv[1]

    user_dict = req.get('https://jsonplaceholder.typicode.com/users/{}'.
                        format(user_id)).json()
    todo_list = req.get('https://jsonplaceholder.typicode.com/users/{}/todos'.
                        format(user_id)).json()

    username = user_dict['username']

    print_list = []

    for task in todo_list:
        task_info = []
        task_info.extend([str(user_id), username,
                          str(task['completed']), task['title']])
        print_list.append(task_info)

    with open('{}.csv'.format(user_id), 'w', newline='') as csvfile:
        my_writer = csv.writer(csvfile, delimiter=',', quoting=csv.QUOTE_ALL)
        for task in print_list:
            my_writer.writerow(task)
