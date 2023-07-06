# author: adrian
import shutil
import time
import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = '1'
import pygame


def print_booting_message():
    print()
    pygame.mixer.init()
    sound = pygame.mixer.Sound('beep.wav')
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
