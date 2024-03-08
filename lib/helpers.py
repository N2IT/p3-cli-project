# lib/helpers.py
import os
from models.workout_routine import WorkoutRoutine
from models.exercise import Exercise 

def clear_screen():
    # For Windows
    if os.name == 'nt':
        os.system('cls')
    # For Linux and Mac
    else:
        os.system('clear')

def wr_by_id_menu():
    print("**************************")
    print("")
    print("Enter the workout routine id to view its details")
    print("OR")
    print(" >>  Type A to create a new Workout Routine")
    print(" >>  Type R to return to the previous menu")
    input(" ")
    return

def list_workout_routines():
    workout_routines = WorkoutRoutine.get_all()
    print("")
    print("")
    print("Here are all workout routines currently on record.")
    print("")
    for workout_routine in workout_routines:
        print(workout_routine)
    wr_by_id_menu()
    

def list_exercises():
    pass
    
def exit_program():
    print("Goodbye!")
    exit()

# def menu():
#     choice = input("> ")
