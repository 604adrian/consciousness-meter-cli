# author: adrian jones
import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = '1'
import pygame
import time

style = "\033[1;38;5;95m"
reset = "\033[0m"


def resource_path(relative_path):
    ''' Gets absolute path to resources'''
    base_path = getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(___file___)))
    return os.path.join(base_path, relative_path)


# usage
antipat_path = resource_path('./antipat.mp3')
conscious_path = resource_path('./conscious.mp3')


def save_user_object():
    global user_object
    with open("user_object.txt", "r") as file:
        user_object = file.read().strip().upper()
        return user_object

def play_sound_one():
    # initate sound
    pygame.mixer.init()
    # anticipation sound
    sound = pygame.mixer.Sound(antipat_path)
    sound.play()
    pygame.time.wait(int(sound.get_length() * 1000))
    return sound


def play_sound_two():
    # conscious sound
    sound = pygame.mixer.Sound(conscious_path)
    sound.play()
    pygame.time.wait(int(sound.get_length() * 1000))
    pygame.mixer.quit()
    print(style + user_object + " IS CONSCIOUS" + reset)



