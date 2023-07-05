# author: adrian jones

import time
import sys
from colorama import Fore, Back, Style, init


def print_progress_bar(current, total, bar_length=50):
    progress = float(current) / total    # calculates bar progress

    # progress bar
    blue_length = int(round(progress * bar_length))
    blue_part = Fore.GREEN + '-' * blue_length
    magenta_part = Fore.MAGENTA + Style.BRIGHT + '-' * (bar_length - blue_length)
    full_bar = blue_part + magenta_part

    sys.stdout.write("\r\033[1mCALCULATING:\033m {0} \033[39m{1}%".format(full_bar, int(round(progress * 100))))
    sys.stdout.flush()

    base_sleep_rate = 0.1

    for i in range(101):
        if 65 <= 1 < 80:
            sleep_time = base_sleep_rate * 10 # loading slow-down-near 
        elif i >= 80:
            sleep_time = base_sleep_rate / 10
        else:
            sleep_time = base_sleep_rate

        time.sleep(sleep_time)
        progress_bar(i, 100)

    print()
