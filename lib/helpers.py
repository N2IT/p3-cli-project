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

def edit_work_routine(routine, exercise_path=None):
    from cli import selected_routine
    print("")
    print("\u001b[36;1mLeave the input blank if you do not wish make a change:\u001b[0m")
    print("")
    title = input("Enter a new title: ")
    equipment = input("Enter new equipment: ")
    if any([title, equipment]):
        try:
            routine.title = title if title else routine.title
            routine.equipment = equipment if equipment else routine.equipment
            print("")
            print(f'\u001b[32;1mThe following has been updated:\u001b[0m')
            print("")
            if title:
                print(f'Routine Title: {title}')
            if equipment:
                print(f'Routine Equipment: {equipment}')
            if exercise_path:
                print("")
                print(f'\u001b[36;1mYou are still editing routine {routine.title}:\u001b[0m')
            routine.update()
        except Exception as exc:
                    print("\u001b[41mError updating routine:\u001b[0m ", exc)
        selected_routine(routine)
    else:
        print("")
        print("\u001b[32;1mNo updates were made.\u001b[0m")
        selected_routine(routine)


def delete_workout_routine(routine):
    print("")
    print(f'\u001b[32;1mRoutine {routine.title} and all associated exercises have been deleted.\u001b[0m')
    WorkoutRoutine.delete(routine)

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

def edit_exercise(exercise, routine_path=None):
    from cli import selected_exercise
    print("")
    print("\u001b[36;1mLeave the input blank if you do not wish make a change:\u001b[0m")
    print("")
    title = input("Enter a new title: ")
    description = input("Enter a new description: ")
    reps = input('Enter a new number of reps for this exercise: ')
    sets = input('Enter a new number of sets for this exercise: ')
    print("")
    routines = WorkoutRoutine.get_all()
    for i, routine in enumerate(routines, start=1):
        print(f'{i}.', routine.title)
    print("")
    w_routine_id = input('Assign your exercise to a new routine: ')
    if any([title, description, reps, sets, w_routine_id]):
        try:
            exercise.title = title if title else exercise.title
            exercise.description = description if description else exercise.description
            if reps:
                if re.compile(r'^\b(100|[0-9]{1,2})\b$').match(reps):
                    exercise.reps = int(reps)
                else:
                    print("")
                    print('\u001b[41mReps value must be numerical.\u001b[0m')
                    return
            else:
                exercise.reps = exercise.reps
            if sets:
                if re.compile(r'^\b(100|[0-9]{1,2})\b$').match(sets):
                    exercise.sets = int(sets)
                else:
                    print("")
                    print('\u001b[41mSets value must be numerical.\u001b[0m')
                    return
            else:
                exercise.sets = exercise.sets
            if w_routine_id:
                if re.compile(r'^(?:[1-9]|[1-9]\d|100)$').match(w_routine_id) and len(routines) >= int(w_routine_id):
                    routines = WorkoutRoutine.get_all()
                    exercise.w_routine_id = routines[int(w_routine_id) - 1].id
                else:
                    print('\u001b[41mThe routine number you selected is invalid. Please try again.\u001b[0m')   
                    return
            else:
                exercise.w_routine_id == exercise.w_routine_id
            print("")
            print(f'\u001b[32;1mThe following has been updated:\u001b[0m')
            print("")
            if title:
                print(f'Exercise Title: {title}')
            if description:
                print(f'Exercise Description: {description}')
            if reps:
                print(f'Exercise Reps: {reps}')
            if sets:
                print(f'Exercise Sets: {sets}')
            if w_routine_id:
                print(f'Exercise Workout Routine: {w_routine_id}')
            print("")
            exercise.update()
            if routine_path:
                print("")
                selected_exercise(exercise)
            else:
                return
        except Exception as exc:
                    print("\u001b[41mError updating exercise:\u001b[0m ", exc)
    else:
        print("")
        print("\u001b[32;1mNo updates were made.\u001b[0m")
        selected_exercise(exercise)
    
def delete_exercise(e):
    for exercise in e:
        Exercise.delete(exercise)