# lib/cli.py
import re
from wr_helpers import (
    clear_screen,
    list_workout_routines_w_menu,
    # wr_menu_options,
    # wr_choice_options,
    # wr_choice_options_menu,
    # edit_work_routine,
    # wr_add_exercise,
    # wr_cut_exercise,
    # wr_delete_exercises,
    # delete_workout_routine,
    # create_workout_routine,
    exit_program
)

from ex_helpers import (
    list_exercises_w_menu,
    ex_choice_options,
    create_exercise,
    ex_choice_options,
    ex_choice_options_menu
)

def login():
    clear_screen()
    username = input("Please enter your name: ")
    if username != "":
            password(username)
    else:
        print(f'{username} is not recognized. Please try again.')
        login()

def password(username):
    print("Please Enter your password.")
    print("HINT: type anything")
    password = input("Password:  ")

    if password != "":
        main(username)
        clear_screen()
    else:
        (f'{password} is not recognized.')
        password(username)


def main(username):
    clear_screen()
    print("")
    print(f"\u001b[36;1mWELCOME TO THE FITNESS CLI {username.upper()}!\u001b[0m")
    while True:
        menu()
        wr_option_regex = re.compile(r'(?i)^wR$')
        exercise_regex = re.compile(r'(?i)^e$')
        x_regex = re.compile(r'(?i)^x$')
        choice = input("> ").strip()
        if wr_option_regex.match(choice):
            if not list_workout_routines_w_menu():
                continue
            # clear_screen()
            # list_workout_routines()
        elif exercise_regex.match(choice):
            if not list_exercises_w_menu():
                continue
        elif x_regex.match(choice):
            exit_program()
        else:
            print(f'{choice} is not valid. Please choose from the options below.')

def menu():
    print("")
    print("**************************")
    print("___________._____________________  ___________ _________ _________ _________ .____    .___ ")
    print("\_   _____/|   \__    ___/\      \ \_   _____//   _____//   _____/ \_   ___ \|    |   |   |")
    print(" |    __)  |   | |    |   /   |   \ |    __)_ \_____  \ \_____  \  /    \  \/|    |   |   |")
    print(" |     \   |   | |    |  /    |    \|        \/        \/        \ \     \___|    |___|   |")
    print(" \___  /   |___| |____|  \____|__  /_______  /_______  /_______  /  \______  /_______ \___|")
    print("     \/                          \/        \/        \/        \/          \/        \/    ")
    print("")
    print("✅ Create your own workout routines")
    print("✅ Create your own exercises")
    print("✅ Set your target number of reps and sets")
    print("✅ Assign exercises to your Workout Routines")
    print("")
    print("Choose from the options below to get started.")
    print("")
    print(" >> Type WR to view all WorkoutRoutines.")
    print(" >> Type E to view all Exercises.")
    print(" >> Type X to exit program.")
    print("")
    print("**************************")
        



if __name__ == "__main__":
    login()
