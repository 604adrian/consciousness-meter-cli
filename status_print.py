# author: adrian jones

style = "\033[1;38;5;95m"
reset = "\033[0m"

def print_status():
    full_prompt = style + "STATUS: " + reset
    print(style + full_prompt + reset, end="")
    return full_prompt



