"""
Description:
    A Python script that, using this REST API
(https://intranet.hbtn.io/rltoken/0Ltm_dXy-m4E9jchBrKLVA),
for a given employee ID, returns information about
his/her TODO list progress.
"""
if __name__ == "__main__":
    import requests as req
    from sys import argv


    user_id = argv[1]

    user_dict = req.get('https://jsonplaceholder.typicode.com/users/{}'.format(user_id)).json()
    todo_list = req.get('https://jsonplaceholder.typicode.com/users/{}/todos'.format(user_id)).json()

    completed_tasks = []
    total_tasks = len(todo_list)
    total_complete = 0
    
    for task in todo_list:
        if task['completed'] == True:
            total_complete += 1
            completed_tasks.append(task['title'])

    print('Employee {} is done with tasks({}/{}):'.format(user_dict['name'], total_complete, total_tasks))
    
    for task in completed_tasks:
        print('\t', task)
