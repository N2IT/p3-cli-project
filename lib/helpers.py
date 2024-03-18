# lib/helpers.py
import os
import re
from models.user import User
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
    user = User.get_all()
    confirmation = input("\u001b[43mAre you sure you wish to exit?\u001b[0m Y/N ")
    if re.compile(r'(?i)^y$').match(confirmation):
        print("")
        print(f"\u001b[36;1mHope you enjoyed using FITNESS CLI {user[0].name.upper()}!\u001b[0m")
        print("")
        print("**************************")
        print("___________._____________________  ___________ _________ _________ _________ .____    .___ ")
        print("\_   _____/|   \__    ___/\      \ \_   _____//   _____//   _____/ \_   ___ \|    |   |   |")
        print(" |    __)  |   | |    |   /   |   \ |    __)_ \_____  \ \_____  \  /    \  \/|    |   |   |")
        print(" |     \   |   | |    |  /    |    \|        \/        \/        \ \     \___|    |___|   |")
        print(" \___  /   |___| |____|  \____|__  /_______  /_______  /_______  /  \______  /_______ \___|")
        print("     \/                          \/        \/        \/        \/          \/        \/    ")
        print("")
        print("")
        User.delete(user[0])
        exit()
    elif re.compile(r'(?i)^n$').match(confirmation):
        return
    else:
        print(f'\u001b[41m{confirmation} is not a valid option. Please try again.\u001b[0m')
        print("")
        print("**************************")
        print("")

def create_workout_routine(exercise=None):
    title = input(f'Enter the name of the new workout routine: ')
    equipment = input(f'Enter the equipment of the new routine: ')
    try:
        routine = WorkoutRoutine.create(title, equipment)
        print("")
        print(f'\u001b[32;1mSuccess! {routine.title} has been created!\u001b[0m')
        print("")
    except Exception as exc:
        print("\u001b[41mError creating workout routine:\u001b[0m ", exc)
    if exercise:
        print("")
        exercise.w_routine_id = routine.id
        exercise.update()
        print("")
        print(f'Exercise {exercise.title} is now associated to your new routine, {routine.title}.')
        print(f'\u001b[36;1mYou are still editing exercise {exercise.title}:\u001b[0m')
        edit_exercise(exercise)
    return

def create_exercise(routine=None):
    print("")
    print("You have opted to create a new exercise.")
    title = input('Enter a title for your exercise: ')
    description = input('Enter a description of your exercise: ')
    reps = input('Enter the target number of reps for your exercise: ')
    sets = input('Enter the target number of sets for your exercise: ')
    if routine:
        w_routine_id = routine.id
    else:
        print("")
        print(f'\u001b[36;1mYou will need to assign this exercise to a routine.\u001b[0m')
        WorkoutRoutine.get_all()
        routines = WorkoutRoutine.all
        for i, routine in enumerate(routines.values(), start=1):
            print(f'{i}.', routine.title)
        print("")
        w_routine_id = input('Enter the routine you wish to apply this exercise: ')
    try:
        new_exercise = Exercise.create(title, description, int(reps), int(sets), int(w_routine_id))
        print("")
        print(f'\u001b[32;1mSuccess! Your new exercise, {new_exercise.title} has been created!\u001b[0m')
        print("")
    except Exception as exc:
        print("")
        print("\u001b[41mError creating exercise:\u001b[0m ", exc)
        print("")
    print("")

def edit_work_routine(routine):
    from cli import wr_choice_options
    print("")
    print("\u001b[36;1mChoose from the options below.\u001b[0m")
    print("")
    decision = input(f"  >>  Type T to update {routine.title}'s title:\n  >>  Type E to update {routine.title}'s equipment:\n  >>  Type B to update both:\n  >>  Type X to edit an exercise of {routine.title}:\n  >>  Type R to return to previous menu\n\n**************************\n  >> ")
    if re.compile(r'(?i)^t$').match(decision):
        try:
            title = input("Enter the workout routine's new title: ")
            routine.title = title
            print("")
            print(f'\u001b[32;1mSuccess! {routine.title} has been updated!\u001b[0m')
        except Exception as exc:
            print("\u001b[41mError editing workout routine:\u001b[0m ", exc)
    elif re.compile(r'(?i)^e$').match(decision):
        try:
            equipment = input("Enter the workout routine's new equipment: ")
            routine.equipment = equipment
            print(f'\u001b[32;1mSuccess! {routine.equipment} has been updated!\u001b[0m')
        except Exception as exc:
            print("\u001b[41mError editing workout routine:\u001b[0m ", exc)
    elif re.compile(r'(?i)^b$').match(decision):
        try:
            title = input("Enter the workout routine's new title: ")
            routine.title = title
            equipment = input("Enter the workout routine's new equipment: ")
            routine.equipment = equipment
        except Exception as exc:
            print("\u001b[41mError editing workout routine:\u001b[0m ", exc)
    elif re.compile(r'(?i)^x$').match(decision):
        if routine.exercises():
            for i, exercise in enumerate(routine.exercises(), start=1):
                print(f'     {i}.', exercise.title)
            choice = input("Please choose which exercise you wish to edit: ")
            if re.compile(r'^(?:[1-9]|[1-9]\d|100)$').match(choice) and len(routine.exercises()) >= int(choice):
                from cli import countdown_timer_exercises
                choice = int(choice)
                print("")
                exercise = routine.exercises()[choice - 1]
                print(f'You have selected to edit the exercise titled: {exercise.title}. ')
                print("")
                seconds = 3
                countdown_timer_exercises(seconds, exercise)
                return
            else:
                print(f'\u001b[41m{choice} not a valid option.\u001b[0m')
        else:
            print("There are currently 0 exercises associated to this routine.")
    elif re.compile(r'(?i)^r$').match(decision):
        return
    else:
        print(f'\u001b[41mWorkout Routine {id} not found.\u001b[0m')
    routine.update()
    print("")
    edit_work_routine(routine)


def delete_workout_routine(routine):
    print("")
    print(f'\u001b[32;1mRoutine {routine.title} and all associated exercises have been deleted.\u001b[0m')
    WorkoutRoutine.delete(routine)

def edit_exercise(exercise):
    decision = input(f"What would you like to update?        \n  >>  Type T to update {exercise.title}'s title:\n  >>  Type D to update {exercise.title}'s description:\n  >>  Type P for reps:\n  >>  Type S for sets:\n  >>  Type W for workout routine id:\n  >>  Type R for previous menu:\n\n**************************\n  >> ")
    print("")
    if re.compile(r'(?i)^t$').match(decision):
        try:
            title = input("Enter a new title: ")
            exercise.title = title
            print("")
            print(f'\u001b[32;1mSuccess! The exercise title, {exercise.title}, from routine number {exercise.w_routine_id}  has been updated!\u001b[0m')
            print("")
        except Exception as exc:
                print("\u001b[41mError updating exercise:\u001b[0m ", exc)
    elif re.compile(r'(?i)^d$').match(decision):
        try:
            description = input("Enter a new description: ")
            exercise.description = description    
            print("")    
            print(f'\u001b[32;1mSuccess! The {exercise.description} has been updated on exercise {exercise.title}.\u001b[0m')
            print("")
        except Exception as exc:
                print("\u001b[41mError updating exercise:\u001b[0m ", exc)
    elif re.compile(r'(?i)^p$').match(decision):
        try:
            reps = input('Enter a new number of reps for this exercise: ')
            exercise.reps = int(reps)
            print("")
            print(f'\u001b[32;1mSuccess! The number of reps have been updated to {exercise.reps} for {exercise.title}.\u001b[0m')
            print("")
        except Exception as exc:
                print("\u001b[41mError updating exercise:\u001b[0m ", exc)
    elif re.compile(r'(?i)^s$').match(decision):
        try:
            sets = input('Enter a new number of sets for this exercise: ')
            exercise.sets = int(sets)
            print("")
            print(f'\u001b[32;1mSuccess! The number of sets has been updated to {exercise.sets} for exercise {exercise.title}.\u001b[0m')
            print("")
        except Exception as exc:
                print("\u001b[41mError updating exercise:\u001b[0m ", exc)        
    elif re.compile(r'(?i)^w$').match(decision):
        print("")
        option = input(f'Would you like to create a new Workout Routine for this exercise or assign to an existing?\n  >>  Type N for New | Type E for Exisiting: ')
        print("")
        if re.compile(r'(?i)^n$').match(option):
            print("")
            create_workout_routine(exercise)
        elif re.compile(r'(?i)^e$').match(option):
            WorkoutRoutine.get_all()
            routines = WorkoutRoutine.all
            for i, routine in enumerate(routines.values(), start=1):
                print(f'{i}.', routine.title)
            print("")
            w_routine_id = input(f'Please select which routine you would like to assign the exercise: ')
            if re.compile(r'^(?:[1-9]|[1-9]\d|100)$').match(w_routine_id) and len(routines) >= int(w_routine_id):
                exercise.w_routine_id = int(w_routine_id)
                print("")
                print(f'\u001b[32;1mSuccess! {exercise.title} has been reassigned to routine number {exercise.w_routine_id}.\u001b[0m')
                print("")
        else:
            print(f'\u001b[41m{choice} is not a valid option. Please try again.\u001b[0m')
    elif re.compile(r'(?i)^r$').match(decision):
        return
    else:
        print(f'\u001b[41m{decision} is not a valid option. Please try again.\u001b[0m')
    exercise.update()
    edit_exercise(exercise)
    
def delete_exercise(e):
    for exercise in e:
        Exercise.delete(exercise)