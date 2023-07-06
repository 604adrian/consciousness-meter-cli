# author: adrian jones
import time
import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = '1'
import pygame

style = "\033[1;38;5;95m"
reset = "\033[0m"

def print_status():
    pygame.mixer.init()
    sound = pygame.mixer.Sound('beep.wav')
    full_prompt = "STATUS:"
    for char in full_prompt:
        sound.play()
        print(style + char + reset, end='', flush=True)
        time.sleep(0.1)
    print(' ', end='')
    return full_prompt



