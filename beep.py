# author: adrian jones
import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = '1'
import pygame

def play_beep():
    pygame.mixer.init()
    sound = pygame.mixer.Sound('beep.ogg')
    sound.play()
    pygame.time.wait(int(sound.get_length() * 1000))
    pygame.mixer.quit()
