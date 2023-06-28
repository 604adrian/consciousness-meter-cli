# author: adrian jones
import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = '1'
import pygame

pygame.mixer.init()
sound = pygame.mixer.Sound('button.mp3')
sound.play()
pygame.time.wait(int(sound.get_length() * 1000))
pygame.mixer.quit()
