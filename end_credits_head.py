# author: adrian
import shutil

# printing the weird ANSI code stuff
bold = "\033[1m"
reset = "\033[0m"
invar = "END CREDITS"
message = bold + invar + reset

# defining columns for centering
columns = shutil.get_terminal_size().columns

# print 
print()
print(message.center(columns))
