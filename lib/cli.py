# lib/cli.py
import re
from helpers import (
    exit_program,
    wr_options,
    clear_screen,
    list_workout_routines,
    list_exercises,
    create_workout_routine,

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
        choice = input("> ").strip()
        if wr_option_regex.match(choice):
            list_workout_routines()
        elif choice == "E" or choice == "e":
            list_exercises()
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
