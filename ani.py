import time
import sys
import threading
import random

def spinning_cursor():
    while True:
        for cursor in '|/-\\':
            yield cursor

def animate(stop_event):
    spinner = spinning_cursor()
    while not stop_event.is_set():
        sys.stdout.write(next(spinner))
        sys.stdout.flush()
        time.sleep(0.1)
        sys.stdout.write('\b') # erase the last written character

def print_scanning_process(item_to_scan):
    '''
    Prints the loading/checkmark animation next to a string
    '''
    print("\033[1;38;5;95m" + item_to_scan + "\033[0m", end=" ")

    stop_event = threading.Event()

    # Start the loading animation
    t = threading.Thread(target=animate, args=(stop_event,))
    t.start()

    # Generate random time time intervals for loading
    random_interval = random.randint(0, 4);
    time.sleep(random_interval) # replace with your actual work

    # Stop the loading animation
    stop_event.set()
    t.join()

    # Print green checkmark
    print("\033[32m\u2714\033[0m")

print()
print_scanning_process(" SCANNING VITALS: ")
print_scanning_process(" SCANNING FOR ZOMBIE PROCESSES: ")
print_scanning_process(" SCANNING FOR ZOMBIE BLUES: ")
print_scanning_process(" SCANNING MICROTUBIALS: ")
print_scanning_process(" EXTRACTING GODEL'S THEOREM: ")
print_scanning_process(" EXTRACTING SECRET SAUCE: ")
print_scanning_process(" PROCESSING INPUT: ")
print()


