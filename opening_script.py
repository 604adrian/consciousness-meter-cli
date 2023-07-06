#!/usr/bin/env python3
# author: adrian jones

import inquirer
import subprocess
import os
import time
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = '1'
import pygame


def opening():
    pygame.mixer.init()
    click_sound = pygame.mixer.Sound('check.mp3')
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
        click_sound.play()
        time.sleep(1)
        return 'illusionist'
    elif answers['options'] == 'panpsychist mode':
        click_sound.play()
        time.sleep(1)
        return 'panpsychist'

