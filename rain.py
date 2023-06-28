import random
import time
import os

# The characters that will be used in the digital rain
characters = list("0123456789ABCDEF")

# ANSI escape codes for different shades of red and reset
colors = [
    "\033[38;2;255;0;0m",  # Bright red
    "\033[38;2;200;0;0m",  # Less bright red
    "\033[38;2;150;0;0m",  # Even less bright red
    "\033[38;2;100;0;0m",  # Barely red
    "\033[0m"  # Reset to terminal default color
]

# Start time
start_time = time.time()

# Initialize lines with reset color
lines = []

while True:
    # Insert a new line at the top
    lines.insert(0, colors[random.randint(0, 3)] + "".join(random.choice(characters) for _ in range(os.get_terminal_size().columns)))

    # If we have too many lines, remove the oldest line
    if len(lines) > 10:
        lines.pop()

    # Print all lines
    print("\n".join(lines))

    # Wait for a short period of time
    time.sleep(0.1)

    # If 10 seconds have passed, break the loop
    if time.time() - start_time > 10:
        break

