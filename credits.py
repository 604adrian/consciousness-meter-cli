# author: adrian jones

import time
import os
from collections import deque
import textwrap
import subprocess
import shutil
import sys
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = '1'
import pygame


def print_end_credits(text_file, lines_to_print, music_file):
    # music
    pygame.mixer.init()
    pygame.mixer.music.load(music_file)
    pygame.mixer.music.play(-1)

    # print heading
    # printing the weird ANSI code stuff
    bold = "\033[1m"
    reset = "\033[0m"
    invar = "END CREDITS"
    message = bold + invar + reset

    # defining columns for centering
    columns = shutil.get_terminal_size().columns

    # print 
    print()
    print(message.center(columns))
    time.sleep(0.6)
    print()
    time.sleep(0.6)

    # the credits
    with open(text_file, 'r') as credits:
        text = credits.read()

    # defining the width of terminal
    terminal_width = os.get_terminal_size().columns

    # splitting file into lines
    lines = text.split('\n')

    # for lines that exceed width of terminal
    wrapped_lines = []
    for line in lines:
        if len(line) > terminal_width:
            wrapped_lines.extend(textwrap.wrap(line, width=terminal_width))
        else:
            wrapped_lines.append(line)

    # scrolling effect to make it look movie credits
    for line in wrapped_lines:
        print(line)
        time.sleep(0.5)

    # stop the sound
    pygame.mixer.music.stop()


