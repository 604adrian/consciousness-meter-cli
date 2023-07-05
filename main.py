# author: adrian jones


# modules to import
import os
import sys
import subprocess
import os
import time
import shutil
import random
import inquirer
from colorama import Fore, Back, Style, init
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = '1'
import pygame

# other python files to import
from opening_script import opening
from ani import spinning_cursor, animate, print_scanning_process
import beep
import credits
from digital_rain import print_digital_rain
import end_credits_head
import heading_end
import heading_ill
import heading_pan
from loading_bar import print_progress_bar
from prompt import get_object, print_object_status
import second_menu
import second_menu_pan
import shut_down
import status_ill
import status_pan
import status_print


def print_scanner_output():
    '''
    The scanner output screen. It mimics a loading screen
    '''
    print()
    print_scanning_process(" SCANNING VITALS: ")
    print_scanning_process(" SCANNING FOR ZOMBIE PROCESSES: ")
    print_scanning_process(" SCANNING FOR ZOMBIE BLUES: ")
    print_scanning_process(" SCANNING MICROTUBIALS: ")
    print_scanning_process(" EXTRACTING GODEL'S THEOREM: ")
    print_scanning_process(" EXTRACTING SECRET SAUCE: ")
    print_scanning_process(" PROCESSING INPUT: ")
    print()


def run_common_processes():
    '''
    Processes that are run in a mode, but do not change between modes
    '''
    print_digital_rain()

    # loading bar
    os.chmod('./animation.sh', 0o755)
    subprocess.run(['./animation.sh'])
    beep.play_beep()

    # prompt
    user_object = str()
    get_object()
    print_object_status()
    print("\033[1;38;5;95mOBJECT: \033[0m ", user_object)

    # print scanner output
    print_scanner_output()

    # loading bar
    init(autoreset=True)    # init colorama
    base_sleep_rate = 0.1
    for i in range(101):
        if 65 <= 1 < 80:
            sleep_time = base_sleep_rate * 10 # loading slow-down-near 
        elif i >= 80:
            sleep_time = base_sleep_rate / 10
        else:
            sleep_time = base_sleep_rate
            time.sleep(sleep_time)
        print_progress_bar(i, 100)
    print()

    # print status
    status_print.print_status()
    style = "\033[1;38;5;95m"
    reset = "\033[0m"


def run_illusionist():
    '''
    What runs in illusionism mode
    '''
    # startup screen
    print()
    heading_ill.print_booting_message()

    run_common_processes()

    # the illusionism specific processes
    status_ill.save_user_object()
    status_ill.play_sound_one()
    print('\033[1;31mⓧ\033[0m')
    status_ill.play_sound_two()
    print()

    second_option = second_menu.get_second_option()
    if second_option == 'illusionist2':
        run_illusionist()
    elif second_option == 'switch_modes':
        choose_modes()
    elif second_option == 'turn_off':
        shut_off()


def run_panpsychist():
    '''
    What runs in pansychist mode
    '''
    print()
    heading_pan.print_startup_message()

    run_common_processes()

    # the panpscyhist specific processes
    style = "\033[1;38;5;95m"
    reset = "\033[0m"
    status_pan.save_user_object()
    status_pan.play_sound_one()
    print('\033[32m\u2714\033[0m')
    status_pan.play_sound_two()
    print()

    # second menu
    second_option_pan = second_menu_pan.get_second_option_pan()
    if second_option_pan == 'panpsychist':
        run_panpsychist()
    elif second_option_pan == 'switch_modes':
        choose_modes()
    elif second_option_pan == 'turn_off':
        shut_off()


def choose_modes():
    '''
    Menu for choosing which mode to bootup in
    '''
    status = opening()
    if status == 'illusionist':
        run_illusionist()
    elif status == 'panpsychist':
        run_panpsychist()


def shut_off():
    '''
    The shutoff sequence
    '''
    # print shufoff heading
    heading_end.print_end_heading()
    shut_down.shut_down()

    # closing animation
    os.chmod('./closing_ani.sh', 0o755)
    subprocess.run(['./animation.sh'])

    # print end credits
    credits.print_end_credits('./credits.txt', 15, 'bach.mp3')

    # fini
    bold = "\033[1m"
    reset = "\033[0m"
    invar = "FINI"
    message = bold + invar + reset
    columns = shutil.get_terminal_size().columns
    print()
    print(message.center(columns))


def main():
    choose_modes()


if __name__ == '__main__':
    main()
