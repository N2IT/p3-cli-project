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
                choice = int(choice)
                print("")
                exercise = routine.exercises()[choice - 1]
                print(f'You have selected to edit the exercise titled: {exercise.title}. ')
                print("")
                edit_exercise(exercise, routine)
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

def edit_exercise(exercise, routine_path=None):
    breakpoint()
    from cli import ex_choice_options
    print('Leave input blank to keep exercise item as is.')
    try:
        title = input("Enter a new title: ")
        if title == "":
            exercise.title = exercise.title
        else:
            exercise.title = title
        description = input("Enter a new description: ")
        if description == "":
            exercise.description = exercise.description
        else:
            exercise.description = description
        reps = input('Enter a new number of reps for this exercise: ')
        if reps == "":
            exercise.reps = exercise.reps
        else:
            if re.compile(r'^\b(100|[0-9]{1,2})\b$').match(reps):
                exercise.reps = int(reps)
            else:
                print("")
                print('\u001b[41mReps value must be numerical.\u001b[0m')
                return
            
        sets = input('Enter a new number of sets for this exercise: ')
        if sets == "":
            exercise.sets = exercise.sets
        else:
            if re.compile(r'^\b(100|[0-9]{1,2})\b$').match(sets):
                exercise.sets = int(sets)
            else:
                print("")
                print('\u001b[41mSets value must be numerical.\u001b[0m')
                return
            
        print("")
        routines = WorkoutRoutine.get_all()
        for i, routine in enumerate(routines, start=1):
            print(f'{i}.', routine.title)
        print("")
        w_routine_id = input('Assign your exercise to a new routine: ')
        if w_routine_id == "":
            exercise.w_routine_id == exercise.w_routine_id
        else:
            if re.compile(r'^(?:[1-9]|[1-9]\d|100)$').match(w_routine_id) and len(routines) >= int(w_routine_id):
                breakpoint()
                routines = WorkoutRoutine.get_all()
                exercise.w_routine_id = routines[int(w_routine_id) - 1].id
            else:
                print('\u001b[41mThe routine number you selected is invalid. Please try again.\u001b[0m')   
                return
        exercise.update()
        print("")
        print(f'\u001b[32;1mExercise {exercise.title} has been updated.\u001b[0m')
        print("")
        print(f'Exercise Title: {exercise.title}')
        print(f'Exercise Description: {exercise.description}')
        print(f'Exercise Reps: {exercise.reps}')
        print(f'Exercise Sets: {exercise.sets}')
        print("")
        breakpoint()
        if routine_path:
            print("")
            print(f'\u001b[36;1mYou are still editing exercise {exercise.title}:\u001b[0m')
            print("")
            ex_choice_options(exercise)
        else:
            return
    except Exception as exc:
                print("\u001b[41mError updating exercise:\u001b[0m ", exc)
    
def delete_exercise(e):
    for exercise in e:
        Exercise.delete(exercise)