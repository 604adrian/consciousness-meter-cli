# author: adrian jones

import inquirer
import subprocess
import os
import time
import sys


# making sure permissions are in order
# os.chmod('./2illusionist.sh', 0o755)
# os.chmod('./menu.sh', 0o755)
# os.chmod('./shut_down.sh', 0o755)


def get_second_option():
    time.sleep(1)
    print()
    print("Navigate with your arrow keys.")
    questions = [
        inquirer.List('options',
                      message="\033[1m" + "HOW WOULD YOU LIKE TO CONTINUE?" + "\033[0m",
                      choices=["run again", "switch modes", "turn off"],
                ),
    ]

    answers = inquirer.prompt(questions)

    if answers['options'] == 'run again':
        return 'illusionist2'
        # subprocess.call(['./2illusionist.sh'])

    elif answers['options'] == 'switch modes':
        return 'switch_modes'
        # subprocess.call(['./menu.sh'])

    elif answers['options'] == 'turn off':
        return 'turn_off'
        # subprocess.call(['./shut_down.sh'])
