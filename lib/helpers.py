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
    confirmation = input("\u001b[43mAre you sure you wish to exit?\u001b[0m Y/N ")
    if re.compile(r'(?i)^y$').match(confirmation):
        print("Goodbye!")
        exit()
    elif re.compile(r'(?i)^n$').match(confirmation):
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


def edit_work_routine(routine):
    print("")
    print("\u001b[36;1mChoose from the options below.\u001b[0m")
    print("")
    decision = input("  >>  Type T to update title:\n  >>  Type E to update equipment:\n  >>  Type B to update both:\n  >>  Type X to edit an exercise:\n\n**************************\n  >> ")
    if re.compile(r'(?i)^t$').match(decision):
        title = input("Enter the workout routine's new title: ")
        routine.title = title
        print("")
        print(f'\u001b[32;1mSuccess! {routine.title} has been updated!\u001b[0m')
    elif re.compile(r'(?i)^e$').match(decision):
        equipment = input("Enter the workout routine's new equipment: ")
        routine.equipment = equipment
        print(f'\u001b[32;1mSuccess! {routine.euipment} has been updated!\u001b[0m')
    elif re.compile(r'(?i)^b$').match(decision):
        title = input("Enter the workout routine's new title: ")
        routine.title = title
        equipment = input("Enter the workout routine's new equipment: ")
        routine.equipment = equipment
    elif re.compile(r'(?i)^x$').match(decision):
        if routine.exercises():
            for i, exercise in enumerate(routine.exercises(), start=1):
                print(f'     {i}.', exercise.title)
            choice = input("Please choose which exercise you wish to edit: ")
            if re.compile(r'^\d{1,3}$').match(choice) and len(routine.exercises) >= int(choice):
                breakpoint()
                print(f'You have selected to edit ')
                return
        else:
            print("There are currently 0 exercises associated to this routine.")


    else:
        print(f'\u001b[41mWorkout Routine {id} not found.\u001b[0m')
    routine.update()
    print("")
    print(f'You are still editing routine {routine.title}')