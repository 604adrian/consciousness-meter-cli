#!/bin/bash

# Define the animation sequence
chars="/-\|"

# Hide the cursor
tput civis

# Start time
SECONDS=0
duration=10  # duration in seconds

# aesthetic gap
echo 

# Loop until duration has passed
while (( SECONDS < duration )); do
  for (( i=0; i<${#chars}; i++ )); do
    # Break the loop if duration has passed
    [[ $SECONDS -ge $duration ]] && break
    sleep 0.5
    echo -en "${BOLD}SCANNING OBJECT.${NC} ${chars:$i:1}" "\r"
  done
done

# Show the cursor
tput cnorm

