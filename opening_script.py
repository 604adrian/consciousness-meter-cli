#!/usr/bin/env python3
# author: adrian jones

import inquirer
import subprocess
import os
import time


def opening():
    # making sure that the relevant BASH scripts are executable
    os.chmod('./illusionist.sh', 0o755)
    os.chmod('./panpsychist.sh', 0o755)

    print("Navigate with your arrow keys.")
    questions = [
        inquirer.List('options',
                      message="\033[1m" +  "RUN CONSCIOUSNESS METER IN: " + "\033[0m",
                      choices=["illusionist mode", "panpsychist mode"],
                ),
    ]

    answers = inquirer.prompt(questions)
    print('Booting consciousness meter up in', answers['options'])

    if answers['options'] == 'illusionist mode':
        subprocess.call(['./illusionist.sh'])
    elif answers['options'] == 'panpsychist mode':
        subprocess.call(['./panpsychist.sh'])


