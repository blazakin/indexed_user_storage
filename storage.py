import os
import json


def data_read():

    file_path = os.path.join(os.path.dirname(__file__), "data.json")
    if os.path.isfile(file_path):
        with open(file_path, "r") as file:
            data = json.loads(file.read())
        return data
    else:
        data_write({})
        return {}


def data_write(data):
    file_path = os.path.join(os.path.dirname(__file__), "data.json")
    with open(file_path, "w") as file:
        file.write(json.dumps(data))


def check_user(username):
    data = data_read()
    if len(data) == 0:
        return False
    for user in data:
        if user == username:
            return True
    return False


def add_user(username):
    data = data_read()
    data[username] = []
    data_write(data)


def add_history(username, history):
    if not check_user(username):
        return False
    else:
        data = data_read()
        user_history = data.get(username)
        user_history.append(history)
        data[username] = user_history
        data_write(data)
        return True


def get_history(username):
    if not check_user(username):
        return False
    else:
        data = data_read()
        return data.get(username)


def get_history_by_index(username, index):
    if not check_user(username):
        return False
    else:
        data = data_read()
        return data.get(username)[index]
