import time
import sys
import threading
import random
import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = '1'
import pygame

def spinning_cursor():
    while True:
        for cursor in '|/-\\':
            yield cursor

def animate(stop_event):
    spinner = spinning_cursor()
    while not stop_event.is_set():
        sys.stdout.write(next(spinner))
        sys.stdout.flush()
        time.sleep(0.1)
        sys.stdout.write('\b') # erase the last written character

def print_scanning_process(item_to_scan):
    '''
    Prints the loading/checkmark animation next to a string
    '''
    pygame.mixer.init()
    typing_sound = pygame.mixer.Sound('beep.wav')
    checkmark_sound = pygame.mixer.Sound('button.mp3')
    for char in item_to_scan:
        typing_sound.play()
        print("\033[1;38;5;95m" + char + "\033[0m", end="", flush=True)
        time.sleep(0.1)

    print(' ', end="")

    stop_event = threading.Event()

    # Start the loading animation
    t = threading.Thread(target=animate, args=(stop_event,))
    t.start()

    # Generate random time time intervals for loading
    random_interval = random.randint(0, 4);
    time.sleep(random_interval) # replace with your actual work

    # Stop the loading animation
    checkmark_sound.play()
    stop_event.set()
    t.join()

    # Print green checkmark
    print("\033[32m\u2714\033[0m")


