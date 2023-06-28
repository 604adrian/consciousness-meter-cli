#!/bin/bash

SCRIPT="consc.py"
COMMAND="consornot"
INSTALL_LOC="/usr/local/bin"

# checking for sudo permissions
# if [ "$EUID" -ne 0 ]
# then echo "Please run this script with sudo."
#    exit
# fi

# check if files are there
# for file in cons.py "${OTHER_PYTHON_SCRIPTS[@]}" "{$BASH_SCRIPTS[@]}" "${REM_FILES[@]}"; do
#   if [ ! -f "$file" ]; then
#       echo "File $file not found! Please make sure you are in the right directory."
#       exit 1
### fi
#done

# making sure its in the right location; might be redundant
# mv consc.py $INSTALL_LOC

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
chmod +x $INSTALL_LOC/$SCRIPT

# making sure all the Bash scripts have the right permissions
#############################################################


# list of all the remaining python scripts
OTHER_PYTHON_SCRIPTS=("2end_credits_head.py" "ani.py" "animation2.py" "beep.py" "credits.py" "digital_rain.py" "end_credits_head.py" "heading_end.py" "heading_ill.py" "heading_pan.py" "loading_bar.py" "matrix_rain.py" "menu.py" "prompt.py" "rain.py" "second_menu.py" "second_menu_pan.py" "shut_down.py" "sound.py" "status_ill.py" "status_pan.py" "status_print.py" "third_menu.py")

# list of python scripts
for SCRIPT_PY in "${OTHER_PYTHON_SCRIPTS[@]}"; do
    chmod +x $SCRIPT_PY
    cp $SCRIPT_PY $INSTALL_LOC/$SCRIPT_PY
done


# list of bash scripts
BASH_SCRIPTS=("2end_credits_head.sh" "2illusionist.sh" "2panpsychist.sh" "animation.sh" "animation2.sh" "bar.sh" "booting.sh" "closing_ani.sh" "end_credits_head.sh" "illusionist.sh" "menu.sh" "panpsychist.sh" "second_menu.sh" "shut_down.sh" "third_menu.sh")

# make bash scripts executable, then move them to install location
for SCRIPT_SH in "${BASH_SCRIPTS[@]}"; do
    chmod +x $SCRIPT_PY
    cp $SCRIPT_SH $INSTALL_LOC/$SCRIPT_SH
done


# list of sound effects and other remaining files
REM_FILES=("antipat.mp3" "bach.mp3" "beep.mp3" "beep.ogg" "button.mp3" "conscious.mp3" "credits.txt" "info.txt" "not_conscious.mp3" "shutdown.mp3" "ufo.wav" "user_object.txt")

# put them in the install location
for REM_FILE in "${REM_FILES[@]}"; do
    cp $REM_FILE $INSTALL_LOC/$REM_FILE
done


# creat a symbolic link for the command
ln -s $INSTALL_LOC/$SCRIPT $INSTALL_LOC/$COMMAND

# last message
echo "Install complete. You can now run the consciousness meter by typing the command 'consornot' into your terminal."

