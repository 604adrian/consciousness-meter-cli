# author: adrian jones
import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = '1'
import pygame


def resource_path(relative_path):
    ''' Gets absolute path to resources'''
    base_path = getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(___file___)))
    return os.path.join(base_path, relative_path)

# usage
beep_ogg_path = resource_path('./beep.ogg')


def play_beep():
    pygame.mixer.init()
    sound = pygame.mixer.Sound('beep.ogg')
    sound.play()
    pygame.time.wait(int(sound.get_length() * 1000))
    pygame.mixer.quit()
