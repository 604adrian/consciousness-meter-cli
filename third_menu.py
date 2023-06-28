# author: adrian jones

import inquirer
import subprocess
import os
import webbrowser

os.chmod('./menu.sh', 0o755)

print("Navigate with your arrow keys.")
questions = [
    inquirer.List('options',
                  message="How would you like to continue?",
                  choices=["info", "credits", "go back"],
            ),
]

answers = inquirer.prompt(questions)

if answers['options'] == 'info':
    info = './info.html'
    current_dir = os.getcwd()
    file_path = os.path.join(current_dir, info)
    webbrowser.open('file://' + file_path)

elif answers['options'] == 'credits':
    credits = './credits.html'
    current_dir = os.getcwd()
    file_path = os.path.join(current_dir, credits)
    webbrowser.open('file://' + file_path)

elif answers['options'] == 'go back':
    os.chmod('./second_menu.sh', 0o755)
    subprocess.call(['./second_menu.sh'])
