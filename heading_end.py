# author: adrian
import shutil

# printing the weird ANSI code stuff
green_bold = "\033[1;32m"
reset = "\033[0m"
invar = "SHUT OFF CONSCIOUSNESS METER"
message = green_bold + invar + reset

# defining columns for centering
columns = shutil.get_terminal_size().columns

# print 
print()
print(message.center(columns))
