# author: adrian
import shutil


def print_startup_message():
# printing the weird ANSI code stuff
    green_bold = "\033[1;32m"
    reset = "\033[0m"
    invar = "BOOTING CONSCIOUSNESS METER IN "
    mode = "PANPSYCHIST MODE"
    message = green_bold + invar + mode + reset

# defining columns for centering
    columns = shutil.get_terminal_size().columns

