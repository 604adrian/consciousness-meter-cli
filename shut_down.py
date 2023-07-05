# author: adrian jones

import random
import time
import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = '1'

import pygame

def shut_down():
    time.sleep(1)

# the sound effects
    pygame.mixer.init()
    sound = pygame.mixer.Sound("shutdown.mp3")
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

