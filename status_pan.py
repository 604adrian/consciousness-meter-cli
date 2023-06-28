# author: adrian jones
import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = '1'
import pygame
import time

style = "\033[1;38;5;95m"
reset = "\033[0m"

def save_user_object():
    global user_object
    with open("user_object.txt", "r") as file:
        user_object = file.read().strip().upper()
        return user_object

def play_sound_one():
    # initate sound
    pygame.mixer.init()
    # anticipation sound
    sound = pygame.mixer.Sound('antipat.mp3')
    sound.play()
    pygame.time.wait(int(sound.get_length() * 1000))
    return sound


def play_sound_two():
    # conscious sound
    sound = pygame.mixer.Sound('conscious.mp3')
    sound.play()
    pygame.time.wait(int(sound.get_length() * 1000))
    pygame.mixer.quit()
    print(style + user_object + " IS CONSCIOUS" + reset)


def main():
    save_user_object()
    play_sound_one()
    print('\033[32m\u2714\033[0m')
    play_sound_two()
    print()


if __name__ == "__main__":
    main()
