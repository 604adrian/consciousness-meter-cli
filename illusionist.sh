#!/bin/bash

# call heading
python3 heading_ill.py

# call digital rain
python3 digital_rain.py

# loading script
./animation.sh

# car unlock sound
python3 beep.py

# call prompt
python3 prompt.py

# loading animation
python3 ani.py

# loading bar
python3 loading_bar.py

# load the print_status
python3 status_print.py

# load the verdict
python3 status_ill.py

# load the second menu
python3 second_menu.py
