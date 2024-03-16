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
    from cli import wr_choice_options
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
        print(f'\u001b[32;1mSuccess! {routine.equipment} has been updated!\u001b[0m')
    elif re.compile(r'(?i)^b$').match(decision):
        title = input("Enter the workout routine's new title: ")
        routine.title = title
        equipment = input("Enter the workout routine's new equipment: ")
        routine.equipment = equipment
    elif re.compile(r'(?i)^x$').match(decision):
        if routine.exercises():
            for i, exercise in enumerate(routine.exercises(), start=1):
                print(f'     {i}.', exercise.title)
            # breakpoint()
            choice = input("Please choose which exercise you wish to edit: ")
            if re.compile(r'^\d{1,3}$').match(choice) and len(routine.exercises()) >= int(choice):
                choice = int(choice)
                print("")
                print(f'You have selected to edit the exercise titled: {routine.exercises()[(choice - 1)].title}. ')
                print("")
                edit_exercise(routine.exercises()[(choice - 1)])
                return
            else:
                print(f'\u001b[41m{choice} not a valid option.\u001b[0m')
        else:
            print("There are currently 0 exercises associated to this routine.")
    else:
        print(f'\u001b[41mWorkout Routine {id} not found.\u001b[0m')
    routine.update()
    print("")
    # print(f'You are still editing routine {routine.title}')
    # wr_choice_options(routine)


def edit_exercise(exercise):
    decision = input("What would you like to update?\nType T for title:\nType D for description:\nType R for reps:\nType S for sets:\nType W for workout routine id:\nType A for all:\n\n**************************\n  >> ")
    if re.compile(r'(?i)^t$').match(decision):
        title = input("Enter a new title: ")
        exercise.title = title
        print("")
        print(f'\u001b[32;1mSuccess! The exercise title, {exercise.title}, from routine number {exercise.w_routine_id}  has been updated!\u001b[0m')
        print("")
        return
        
    elif re.compile(r'(?i)^d$').match(decision):
        description = input("Enter a new description: ")
        exercise.description = description    
        print("")    
        print(f'\u001b[32;1mSuccess! The {exercise.description} has been updated on exercise {exercise.title}.\u001b[0m')
        print("")
        
    elif re.compile(r'(?i)^r$').match(decision):
        reps = input('Enter a new number of reps for this exercise: ')
        exercise.reps = int(reps)
        print("")
        print(f'\u001b[32;1mSuccess! The number of reps have been updated to {exercise.reps} for {exercise.title}.\u001b[0m')
        print("")
        
    elif re.compile(r'(?i)^s$').match(decision):
        sets = input('Enter a new number of sets for this exercise: ')
        exercise.sets = int(sets)
        print("")
        print(f'\u001b[32;1mSuccess! The number of sets has been updated to {exercise.sets} for exercise {exercise.title}.\u001b[0m')
        print("")
        
    elif re.compile(r'(?i)^w$').match(decision):
        print("")
        option = input(f'Would you like to create a new Workout Routine for this exercise or assign to an existing?\n  >>  Type N for New | Type E for Exisiting: ')
        print("")
        if re.compile(r'(?i)^n$').match(option):
            print("")
            create_workout_routine()
        elif re.compile(r'(?i)^e$').match(option):
            WorkoutRoutine.get_all()
            routines = WorkoutRoutine.all
            for i, routine in enumerate(routines.values(), start=1):
                print(f'{i}.', routine.title)
            print("")
            w_routine_id = input(f'Please select which routine you would like to assign the exercise: ')
            if re.compile(r'^\d{1,3}$').match(w_routine_id) and len(routines) >= int(w_routine_id):
                exercise.w_routine_id = int(w_routine_id)
                print("")
                print(f'\u001b[32;1mSuccess! {exercise.title} has been reassigned to routine number {exercise.w_routine_id}.\u001b[0m')
                print("")
        else:
            print(f'\u001b[41m{choice} is not a valid option. Please try again.\u001b[0m')
    else:
        print(f'\u001b[41m{choice} is not a valid option. Please try again.\u001b[0m')
    exercise.update()


    
    
    
            
    