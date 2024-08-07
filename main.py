from storage import *

import zmq


def get_option(message):
    start = message.find("Option: ")
    end = message.find(", User: ")
    return message[start+8:end]


def get_user(message):
    start = message.find("User: ")
    end = message.find(", History: ")
    return message[start+6:end]


def get_message_history(message):
    start = message.find("History: ")
    return message[start+9:]


context = zmq.Context()
socket = context.socket(zmq.REP)
socket.bind("tcp://*:5551")

while True:
    message = socket.recv().decode()

    if message == 'Exit':
        break

    option = get_option(message)

    match option:
        case 'Check User':
            user = get_user(message)
            if check_user(user):
                socket.send_string("User exists.")
            else:
                socket.send_string("User does not exist.")

        case 'Add User':
            user = get_user(message)
            add_user(user)
            socket.send_string("User successfully added.")

        case 'Add History':
            user = get_user(message)
            history = get_message_history(message)
            if add_history(user, history):
                socket.send_string("History successfully added.")
            else:
                socket.send_string("User does not exist.")

        case 'Get History':
            user = get_user(message)
            history = get_history(user)
            if history != False:
                socket.send_string(str(history))
            else:
                socket.send_string("User does not exist.")

        case 'Get History By Index':
            user = get_user(message)
            index = int(get_message_history(message))
            history = get_history_by_index(user, index)
            if history != False:
                socket.send_string(str(history))
            else:
                socket.send_string("User does not exist.")

        case _:
            socket.send_string("Invalid Command.")


context.destroy()
