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
    
def list_workout_routines():
    workout_routines = WorkoutRoutine.get_all()
    print("")
    print("Here are all workout routines currently on record.")
    print("")
    wo_id = []
    for workout_routine in workout_routines:
        print(f'ID: {workout_routine.id}, Title: {workout_routine.title}')
        wo_id.append(workout_routine.id)
    while True:
        wr_options()
        choice = input("> ")

        # possibly use RegEx to compile numbers option and match number patters for entering id numbers
            # create regex variable
            # compile
            # match for id numbers entered

        # if choice == "r" or choice == "R":
        #     from cli import menu
        #     menu()
        #     return False
        # elif choice == "A" or choice == "a":
        #     create_workout_routine()
        # elif choice in wo_id:
        #     exercises = WorkoutRoutine.find_by_id(choice)
        #     if exercises:
        #         print(exercises)
        #     else: 
        #         print(f'Workout Routine {choice} not found') 
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
        
def create_workout_routine():
    print('workout routine added!')


def list_exercises():
    pass
    
def exit_program():
    print("Goodbye!")
    exit()

# def menu():
#     choice = input("> ")
