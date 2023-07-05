# author: adrian
import shutil


def print_end_heading():
# printing the weird ANSI code stuff
    green_bold = "\033[1;32m"
    reset = "\033[0m"
    invar = "SHUTING OFF CONSCIOUSNESS METER"
    message = green_bold + invar + reset

# defining columns for centering
    columns = shutil.get_terminal_size().columns

# print 
    print()
    print(message.center(columns))
