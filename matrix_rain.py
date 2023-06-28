import random
import time
import os
import pygame

# Initialize pygame mixer
pygame.mixer.init()
sound = pygame.mixer.Sound('ufo.wav')
sound.play()

characters = list("0123456789ABCDEF")

# Define the number of raindrops and their initial positions
num_raindrops = os.get_terminal_size().columns
raindrop_positions = [random.randint(0, os.get_terminal_size().columns - 1) for _ in range(num_raindrops)]

while pygame.mixer.get_busy():
    # Generate the digital rain lines
    lines = []
    for i in range(os.get_terminal_size().lines):
        line = "".join(random.choice(characters) for _ in range(os.get_terminal_size().columns))
        lines.append(line)

    # Add raindrops to the lines
    for i, position in enumerate(raindrop_positions):
        if position < os.get_terminal_size().columns:
            lines[position] = "\033[32m" + random.choice(characters) + "\033[0m" + lines[position]
        raindrop_positions[i] = (position + 1) % os.get_terminal_size().columns

    # Print the digital rain with raindrops
    print("\033[38;2;255;0;0m" + "\n".join(lines) + "\033[0m")  # Print red lines on black background
    time.sleep(0.05)

# Quit pygame mixer
pygame.mixer.quit()

