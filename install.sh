!#/bin/bash

SCRIPT="cons.py"
COMMAND="consornot"
INSTALL_LOC="/user/local/bin"

# making sure all the Bash scripts have the right permissions
chmod +x 2end_credits_head.sh
chmod +x 2illusionist.sh
chmod +x 2panpsychist.sh
chmod +x animation.sh
chmod +x animation2.sh
chmod +x bar.sh
chmod +x booting.sh
chmod +x closing_ani.sh
chmod +x end_credits_head.sh
chmod +x illusionist.sh
chmod +x menu.sh
chmod +x panpsychist.sh
chmod +x second_menu.sh
chmod +x shut_down.py
chmod +x shut_down.sh
chmod +x shutdown.mp3
chmod +x third_menu.sh


# check for python3
if ! command -v python3 &> /dev/null
then
    echo "Python3 could not be found. Please install Python3 and try again."
    exit
fi

# Check for pip
if ! command -v pip3 &> /dev/null
then
    echo "Pip3 could not be found. Please install pip3 and try again."
    exit
fi


# Check for dependencies
pip3 freeze | grep -q '^inquirer=' || pip3 install inquirer
pip3 freeze | grep -q '^pygame=' || pip3 install pygame

# Make the Python script executable
chmod +x $SCRIPT

# Remove the .py extension and move the script to the 
