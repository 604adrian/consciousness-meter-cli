# author: adrian
import shutil
import time
import os
import sys
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = '1'
import pygame


def resource_path(relative_path):
    ''' Gets absolute path to resources'''
    base_path = getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(__file__)))
    return os.path.join(base_path, relative_path)

# usage
beep_path = resource_path('./beep.wav')


def print_booting_message():
    print()
    pygame.mixer.init()
    sound = pygame.mixer.Sound(beep_path)
# printing the weird ANSI code stuff
    green_bold = "\033[1;32m"
    reset = "\033[0m"
    invar = "BOOTING CONSCIOUSNESS METER IN "
    mode = "ILLUSIONIST MODE"
    message = invar + mode
    i = 0
    padding = (shutil.get_terminal_size().columns - len(message)) // 2
    print(' ' * padding, end='', flush=True)
    while i < len(message):
        sound.play()
        char = message[i]
        item = str(green_bold + char + reset)
        columns = (shutil.get_terminal_size().columns) - (len(message) - i)
        print(item, end='', flush=True)
        time.sleep(0.1)
        i += 1
    print()
