# lib/helpers.py
import os
import re
from models.user import User
from models.workout_routine import WorkoutRoutine
from models.exercise import Exercise


### ###  MISCELLANEOUS  ### ###
def clear_screen():
    # For Windows
    if os.name == 'nt':
        os.system('cls')
    # For Linux and Mac
    else:
        os.system('clear')

def validate_integer_input(input_value):
    try:
        return int(input_value)
    except ValueError:
        raise ValueError("Invalid input: the value must be an integer.")

def validate_w_routine_id(w_routine_id):
    error = "Invalid routine number"
    routines = return_routines()
    if w_routine_id:
        w_routine_id = validate_integer_input(w_routine_id)
        if 0 < w_routine_id <= len(routines):
            w_routine_id = routines[w_routine_id - 1].id
            return w_routine_id
        else:
            return error
    else:
        return None

def check_string(str):
    flag_string = False
    for i in str:
        if i in "abcdefghijklmnopqrstuvwxyz" or i in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
            flag_string = True
    return flag_string

def print_invalid_choice(choice):
    print("")
    print(f'\u001b[41m{choice} is not a valid option.\u001b[0m')
    print("")

def confirmation_to_delete(title, routine = None):
    if routine:
        print("")
        print(f'\u001b[32;1m{title} has been deleted from routine {routine.title}.\u001b[0m')
        print("")
    else:
        print("")
        print(f'\u001b[32;1m{title} has been deleted.\u001b[0m')
        print("")

def declining_to_delete(title):
    print("")
    print("**************************")
    print(f'You have opted not to delete {title}.')
    print("**************************")

def number_selected_from_menu(choice, routines = None):
    choice = validate_integer_input(choice)
    if routines:
        from cli import selected_routine
        if 1 <= choice <= len(return_routines()):
            routine = return_routines()[choice - 1]
            selected_routine(routine)
        else:
            print_invalid_choice(choice)
    else:
        from cli import selected_exercise
        if 1 <= choice <= len(return_exercises()):
            exercise = return_exercises()[choice - 1]
            selected_exercise(exercise)
        else:
            print_invalid_choice(choice)

### ###  ROUTINE MENU ACTION HELPERS  ### ###

def print_routines_list():
    print("")
    print("\u001b[36;1mHere are all workout routines currently on record.\u001b[0m")
    print("")
    routines = WorkoutRoutine.get_all()
    for i, routine in enumerate(routines, start=1):
        print(f'{i}.', routine.title)
    print("")

def return_routines():
    routines = WorkoutRoutine.get_all()
    return routines

def routine_menu_option_d(routine):
    confirmation = input(f'\u001b[43mAre you sure you want to delete {routine.title}?\u001b[0m Y/N ')
    if confirmation.lower() == 'y':
        print("")
        delete_workout_routine(routine)
    elif confirmation.lower() == 'n':
        None
    else:
        print("")
        print(f'\u001b[41m{confirmation} is not a valid option. Please try again.\u001b[0m')
        print("")
        routine_menu_option_d(routine)

def print_selected_routine(routine):
    print("")
    print(f"\u001b[36;1mHere are {routine.title}'s details.\u001b[0m")
    print("")
    print(f'Routine Title: {routine.title}, Routine Equipment: {routine.equipment}')
    if routine.exercises():
        print("Exercises:")
        for i, exercise in enumerate(routine.exercises(), start=1):
            print(f'     {i}.', exercise.title)
    else:
        print("There are currently 0 exercises associated to this routine.")

def cut_solo_exercise_from_routine(routine):
    terminate_exercise = routine.exercises()[0]
    confirmation = input(f'\u001b[43mAre you sure you want to delete {terminate_exercise.title}?\u001b[0m Y/N ')
    if confirmation.lower() == 'y':
        confirmation_to_delete(terminate.exercise.title)
        delete_exercise([terminate_exercise])
    elif confirmation.lower() == 'n':
        declining_to_delete(terminate_exercise.title)
    else:
        print_invalid_choice(confirmation)
        cut_solo_exercise_from_routine(routine)

def cut_selected_exercise_from_routine(routine):
    selection = input(f'Which exercise do you wish to delete? ')
    if check_string(selection):
        print_invalid_choice(selection)
        return
    else:
        terminate_exercise = exercise_number_validation(routine, selection)
        if terminate_exercise:
            confirmation = input(f'\u001b[43mAre you sure you want to delete exercise {selection}?\u001b[0m Y/N ')
            if confirmation.lower() == 'y':
                confirmation_to_delete(terminate_exercise.title, routine)
                delete_exercise([terminate_exercise])
            elif confirmation.lower() == 'n':
                declining_to_delete(terminate_exercise.title)
                return
            else:
                print_invalid_choice(confirmation)
                return
        else:
            return

def create_workout_routine():
    title = input(f'Enter the name of the new workout routine: ')
    equipment = input(f'Enter the equipment of the new routine: ')
    try:
        routine = WorkoutRoutine.create(title, equipment)
        print("")
        print(f'\u001b[32;1mSuccess! {routine.title} has been created!\u001b[0m')
    except Exception as exc:
        print("\u001b[41mError creating workout routine:\u001b[0m ", exc)
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

def edit_solo_exercise_from_routine(routine):
    exercise_to_edit = routine.exercises()[0]
    print("")
    print(f'\u001b[36;1mNow editing {exercise_to_edit.title}\u001b[0m')
    edit_exercise(exercise_to_edit)

def edit_selected_exercise_from_routine(routine):
    selection = input(f'Which exercise do you wish to edit? ')
    if check_string(selection):
        print_invalid_choice(selection)
        return
    else: 
        exercise_to_edit = exercise_number_validation(routine, selection)
        if exercise_to_edit:
            edit_exercise(exercise_to_edit, routine)
        else:
            return


### ###  EXERCISE MENU ACTION HELPERS  ### ###

def print_exercises_list():
    print("")
    print("\u001b[36;1mHere are all exercises currently on record.\u001b[0m")
    print("")
    exercises = Exercise.get_all()
    for i, exercise in enumerate(exercises, start = 1):
        print(f'{i}.', exercise.title)
    print("")
    
def return_exercises():
    exercises = Exercise.get_all()
    return exercises

def print_selected_exercise(exercise):
    exercise = exercise.find_by_id(exercise.id)
    print("")
    print(f'\u001b[36;1mYou are editing exercise {exercise.title}:\u001b[0m')
    print("")
    print(f'Exercise Title: {exercise.title}\nExercise Description: {exercise.description}\nTarget Reps: {exercise.reps}\nTarget Sets: {exercise.sets}')
    print("")

def exercise_menu_option_d(exercise):
    confirmation = input(f'\u001b[43mAre you sure you want to delete {exercise.title}?\u001b[0m Y/N ')
    if confirmation.lower() == 'y':
        confirmation_to_delete(exercise.title)
        delete_exercise([exercise])
    elif confirmation.lower() == 'n':
        from cli import selected_exercise
        declining_to_delete(exercise.title)
        selected_exercise(exercise)
    else:
        print("")
        print(f'\u001b[41m{confirmation} is not a valid option. Please try again.\u001b[0m')
        print("")
        exercise_menu_option_d(exercise)

def exercise_menu_option_v(routine, exercise):
    routine = WorkoutRoutine.find_by_id(exercise.w_routine_id)
    print("")
    print(f'\u001b[36;1mHere are the details of the routine associated to this exercise:\u001b[0m')
    print(f'Routine Title: {routine.title}, Routine Equipment: {routine.equipment}')
    print("")
    confirmation = input(f'Would you like to edit {routine.title}? Y/N ')
    if confirmation.lower() == 'y':
        edit_work_routine(routine, exercise)
    elif confirmation.lower() == 'n':
        None
    else:
        print("")
        print(f'\u001b[41m{confirmation} is not a valid option. Please try again.\u001b[0m')
        print("")
        return

def exercise_number_validation(routine, selection):
    selection = validate_integer_input(selection)
    if 1 <= selection <= len(routine.exercises()):
        exercise = routine.exercises()[selection - 1]
        return exercise
    else:
        print_invalid_choice(selection)

def create_exercise(routine_path=None):
    print("")
    print("\u001b[36;1mYou have opted to create a new exercise.\u001b[0m")
    print("")
    title = input('Enter a title for your exercise: ')
    description = input('Provide details about the exercise. ie. target muscle group or how-to instructions: ')
    reps = input('Enter the target number of reps for your exercise: ')
    sets = input('Enter the target number of sets for your exercise: ')
    if routine_path:
        w_routine_id = routine_path.id
    else:
        print("")
        print(f'\u001b[36;1mYou will need to assign this exercise to a routine.\u001b[0m')
        print_routines_list()
        print("")
        w_routine_id = input('Enter the routine you wish to apply this exercise: ')
        if check_string(w_routine_id):
            print_invalid_choice(w_routine_id)
            return
        else:
            w_routine_id = validate_w_routine_id(w_routine_id)
    if any([title, description, reps, sets, w_routine_id]):
        try:
            new_exercise = Exercise.create(title, description, reps, sets, w_routine_id)
            print("")
            print(f'\u001b[32;1mSuccess! Your new exercise, {new_exercise.title} has been created!\u001b[0m')
            print("")
        except Exception as exc:
            print("")
            print("\u001b[41mError creating exercise:\u001b[0m ", exc)
            print("")
    else:
        print("")
        print('You did not enter any values. Please try again.')
        create_exercise()
    return

def edit_exercise(exercise, routine_path=None):
    from cli import selected_exercise
    print("")
    print("\u001b[36;1mLeave the input blank if you do not wish make a change:\u001b[0m")
    print("")
    title = input("Enter a new title: ")
    description = input("Provide details about the exercise. ie. target muscle group or how-to instructions: ")
    reps = input('Enter a new number of reps for this exercise: ')
    sets = input('Enter a new number of sets for this exercise: ')
    print("")
    print_routines_list()
    w_routine_id = input('Assign your exercise to a new routine: ')
    print("")
    try:
        exercise.title = title if title else exercise.title
        exercise.description = description if description else exercise.description
        exercise.reps = reps if reps else exercise.reps
        exercise.sets = sets if sets else exercise.sets
        exercise.w_routine_id = w_routine_id if validate_w_routine_id(w_routine_id) else exercise.w_routine_id
        if any([title, description, reps, sets, w_routine_id]):
            print("")
            print(f'\u001b[32;1mThe following has been updated:\u001b[0m')
            print("")
            if title:
                print(f'Exercise Title: {exercise.title}')
            if description:
                print(f'Exercise Description: {exercise.description}')
            if reps:
                print(f'Exercise Reps: {exercise.reps}')
            if sets:
                print(f'Exercise Sets: {exercise.sets}')
            if w_routine_id:
                print(f'Exercise Workout Routine: {exercise.w_routine_id}')
            print("")
            exercise.update()
            if routine_path:
                print("")
                selected_exercise(exercise)
            else:
                return
        else:
            print("")
            print("\u001b[32;1mNo updates were made.\u001b[0m")
            return
    except Exception as exc:
        print("\u001b[41mError updating exercise:\u001b[0m ", exc)
        return
    return
    
def delete_exercise(e):
    for exercise in e:
        Exercise.delete(exercise)

def exit_program():
    user = User.get_all()
    confirmation = input("\u001b[43mAre you sure you wish to exit?\u001b[0m Y/N ")
    if confirmation.lower() == 'y':
        clear_screen()
        print("")
        print(f"\u001b[36;1mHope you enjoyed using FITNESS CLI {user[0].name}!\u001b[0m")
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
        print("\u001b[1m”Don’t count the days, make the days count.”\u001b[0m —Muhammad Ali")
        print("")
        print("")
        print("")
        print("")
        print("")
        print("")
        print("")
        print("")
        User.delete(user[0])
        exit()
    elif confirmation.lower() == 'n':
        return
    else:
        print(f'\u001b[41m{confirmation} is not a valid option. Please try again.\u001b[0m')
        print("")
        print("**************************")
        print("")
    