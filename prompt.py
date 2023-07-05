# author: adrian jones

import subprocess


# input for user
def get_object():
    global user_object
    user_object = input("\033[1;38;5;95mINPUT OBJECT TO SCAN: \033[0m")
    with open("user_object.txt", "w") as file:
        file.write(str(user_object))
    return user_object


def print_object_status():
    with open("user_object.txt", "r") as file:
        user_object = file.read().strip().upper()
        return user_object



