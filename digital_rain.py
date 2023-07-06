# author: adrian jones

import random
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
ufo_path = resource_path('./ufo.wav')



def print_digital_rain():
# the sound effects
    pygame.mixer.init()
    sound = pygame.mixer.Sound(ufo_path)
    sound.play()

# the digital rain
    characters = list("0123456789ABCDEF")

# timer
    start_time = time.time()

# will print digital rain when the sound is playing
    while pygame.mixer.get_busy():
        line = "".join(random.choice(characters) for _ in range(os.get_terminal_size().columns))
        print("\033[31m" + line + "\033[0m")  # Print red line on black background
        time.sleep(0.1)

        if time.time() - start_time > 5:  # will stop after 5 seconds
            break

