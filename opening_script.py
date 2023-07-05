#!/usr/bin/env python3
# author: adrian jones

import inquirer
import subprocess
import os
import time


def opening():
    print("Navigate with your arrow keys.")
    questions = [
        inquirer.List('options',
                      message="\033[1m" +  "RUN CONSCIOUSNESS METER IN" + "\033[0m",
                      choices=["illusionist mode", "panpsychist mode"],
                ),
    ]

    answers = inquirer.prompt(questions)
    print('Booting consciousness meter up in', answers['options'])

    if answers['options'] == 'illusionist mode':
        return 'illusionist'
    elif answers['options'] == 'panpsychist mode':
        return 'panpsychist'

