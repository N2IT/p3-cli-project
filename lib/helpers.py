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
    
def list_workout_routines():
    workout_routines = WorkoutRoutine.get_all()
    print("")
    print("Here are all workout routines currently on record.")
    print("")
    wo_id = []
    for workout_routine in workout_routines:
        print(f'ID: {workout_routine.id}, Title: {workout_routine.title}')
        wo_id.append(str(workout_routine.id))
    while True:
        wr_options()
        choice = input("> ").strip()
        ret_choice_regex = re.compile(r'(?i)^r$')
        add_choice_regex = re.compile(r'(?i)^a$')
        if ret_choice_regex.match(choice):
            from cli import menu
            menu()
            return False
        elif add_choice_regex.match(choice):
            create_workout_routine()
        elif choice in wo_id:
            choice = int(choice)
            exercises = WorkoutRoutine.find_by_id(choice)
            if exercises:
                print("")
                print("Here are the workout routine details.")
                print("")
                print(exercises)
                wr_choice_options()
            else: 
                print(f'Workout Routine {choice} not found') 
        else:
            print(f'{choice} is not valid. Please choose again.')

    
def wr_options():
    print("**************************")
    print("")
    print(" >>  Enter the workout routine id to view its details")
    print("                     OR                      ")
    print(" >>  Type A to create a new Workout Routine")
    print(" >>  Type R to return to the previous menu")
    print("")
    print("**************************")

def wr_choice_options():
    while True:
        wr_choice_option_menu()
        choice = input("> ")



def wr_choice_options_menu():
    print("")
    print("Here are the workout routine details.")
    print("")

def create_workout_routine():
    print('workout routine added!')


def list_exercises():
    pass
    
def exit_program():
    print("Goodbye!")
    exit()

# def menu():
#     choice = input("> ")
