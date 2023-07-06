# author: adrian jones
import time
import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = '1'
import pygame

style = "\033[1;38;5;95m"
reset = "\033[0m"


def resource_path(relative_path):
    ''' Gets absolute path to resources'''
    base_path = getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(___file___)))
    return os.path.join(base_path, relative_path)

# usage
beep_path = resource_path('./beep.wav')


def print_status():
    pygame.mixer.init()
    sound = pygame.mixer.Sound(beep_path)
    full_prompt = "STATUS:"
    for char in full_prompt:
        sound.play()
        print(style + char + reset, end='', flush=True)
        time.sleep(0.1)
    print(' ', end='')
    return full_prompt



