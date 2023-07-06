#!/usr/bin/env python3
# author: adrian jones

import inquirer
import subprocess
import os
import time
import sys
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = '1'
import pygame


def resource_path(relative_path):
    ''' Gets absolute path to resources'''
    base_path = getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(__file__)))
    return os.path.join(base_path, relative_path)

# usage
check_path = resource_path('./check.mp3')


def opening():
    pygame.mixer.init()
    click_sound = pygame.mixer.Sound(check_path)
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

