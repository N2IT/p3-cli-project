# lib/helpers.py
import os
import re
from models.workout_routine import WorkoutRoutine
from models.exercise import Exercise 

def clear_screen():
    # For Windows
    if os.name == 'nt':
        os.system('cls')
    # For Linux and Mac
    else:
        os.system('clear')

def exit_program():
    y_regex = re.compile(r'(?i)^y$')
    n_regex = re.compile(r'(?i)^n$')
    confirmation = input("\u001b[43mAre you sure you wish to exit?\u001b[0m Y/N ")
    if y_regex.match(confirmation):
        print("Goodbye!")
        exit()
    elif n_regex.match(confirmation):
        return
    else:
        print(f'\u001b[41m{confirmation} is not a valid option. Please try again.\u001b[0m')
        print("")
        print("**************************")
        print("")

def create_workout_routine():
    title = input(f'Enter the name of the new workout routine: ')
    equipment = input(f'Enter the equipment of the new routine: ')
    try:
        routine = WorkoutRoutine.create(title, equipment)
        print("")
        print(f'\u001b[32;1mSuccess! {routine.title} has been created!\u001b[0m')
        print("")
        print(routine)
        return
    except Exception as exc:
        print("\u001b[41mError creating workout routine:\u001b[0m ", exc)
    return