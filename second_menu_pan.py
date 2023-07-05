# author: adrian jones

import inquirer
import subprocess
import os
import time

def get_second_option_pan():
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
        # os.chmod('./2panpsychist.sh', 0o755)
        # subprocess.call(['./2panpsychist.sh'])
        return 'panpsychist'

    elif answers['options'] == 'switch modes':
        # os.chmod('./menu.sh', 0o755)
        # subprocess.call(['./menu.sh'])
        return 'switch_modes'

    elif answers['options'] == 'turn off':
        # os.chmod('./shut_down.sh', 0o755)
        # subprocess.call(['./shut_down.sh'])
        return 'shut_off'
