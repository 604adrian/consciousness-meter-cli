#!/bin/bash

echo

# Calculate padding
text="BOOTING CONSCIOUSNESS METER"
padding=$(( (cols - ${#text}) /  2 ))

# Print the text centered
printf "%*s%s\n" $padding '' "$text"

# call on python
python3 digital_rain.py
./animation.sh
python3 beep.py

# for finding the width of the terminal
term_width=$(tput cols)

# Define the progress bar length and the character to represent it
bar_length=$((term_width - 10))
bar_char="#"

# Initialize the progress bar
progress_bar=""

# Hide the cursor
tput civis

# Set the background colour
tput setab 2

# Nice aesthetic gap
echo

# Loop to simulate a process
for i in {5..0}; do
    # Add the bar character to the progress bar
    progress_bar+=$bar_char

    # Print the progress bar along with the percentage
    printf "\r[%-${bar_length}s] %d%%" "$progress_bar" $(( (i*100)/bar_length ))

done

# reset terminal attributes back to default
tput op

# Clear the bar
printf "\r%${term_width}s\r" " "

# Bring the cursor back
tput cnorm

# Print a newline at the end
echo

# background process
python3 ani.py



