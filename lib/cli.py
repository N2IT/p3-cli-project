# lib/cli.py
import re
from helpers import (
    clear_screen,
    list_workout_routines,
    wr_options,
    wr_choice_options,
    wr_choice_options_menu,
    edit_work_routine,
    wr_add_exercise,
    wr_cut_exercise,
    wr_delete_exercises,
    delete_workout_routine,
    create_workout_routine,
    list_exercises,
    exit_program,

)

def login():
    clear_screen()
    username = input("Please enter your username: ")
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
    print(f"Welcome {username}!")
    while True:
        menu()
        wr_option_regex = re.compile(r'(?i)^wR$')
        exercise_regex = re.compile(r'(?i)^e$')
        choice = input("> ").strip()
        if wr_option_regex.match(choice):
            if not list_workout_routines():
                continue
            # clear_screen()
            # list_workout_routines()
            
        elif exercise_regex.match(choice):
            if not list_exercises():
                continue

        else:
            print(f'{choice} is not valid. Please choose from the options below.')

def menu():
    print("")
    print("**************************")
    print("")
    print("WELCOME TO THE FITNESS CLI!")
    print("✅ Create your own workout routines")
    print("✅ Create your own exercises")
    print("✅ Set your target number of reps and sets")
    print("✅ Join your exercises to your Workout Routines")
    print("")
    print("See menu options below to get started.")
    print("")
    print(" >> Type WR to view all WorkoutRoutines.")
    print(" >> Type E to view all Exercises.")
    print("")
    print("**************************")
        



if __name__ == "__main__":
    login()
