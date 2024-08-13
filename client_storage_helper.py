import zmq


def send_storage_message(message):
    context = zmq.Context()
    socket = context.socket(zmq.REQ)
    socket.connect("tcp://localhost:5551")

    socket.send_string(message)

    message = socket.recv()
    return message.decode()


def end_storage_server():
    context = zmq.Context()
    socket = context.socket(zmq.REQ)
    socket.connect("tcp://localhost:5551")
    socket.send_string("Exit")


def storage_check_user(user):
    return send_storage_message(f"Option: Check User, User: {user}, History: NA")


def storage_add_user(user):
    return send_storage_message(f"Option: Add User, User: {user}, History: NA")


def storage_add_history(user, history):
    return send_storage_message(f"Option: Add History, User: {
        user}, History: {history}")


def storage_get_history(user):
    return send_storage_message(f"Option: Get History, User: {user}, History: NA")


def storage_get_history_by_index(user, index):
    return send_storage_message(f"Option: Get History By Index, User: {
        user}, History: {index}")
