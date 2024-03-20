# lib/cli.py
import re
import time
from models.user import User
from models.workout_routine import WorkoutRoutine
from models.exercise import Exercise 
from helpers import (
    clear_screen,
    exit_program,
    create_workout_routine,
    edit_work_routine,
    delete_workout_routine,
    edit_exercise,
    create_exercise,
    delete_exercise
)

def check_string(str):
    flag_string = False
    for i in str:
        if i in "abcdefghijklmnopqrstuvwxyz" or i in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
            flag_string = True
    return flag_string

def login():
    clear_screen()
    name = input("Please enter your name: ")
    try:
        user = User.create(name)
        main(user)
    except Exception as exc:
        print("\u001b[41mError creating user:\u001b[0m ", exc)
    
def main(user):
    clear_screen()
    print("")
    print(f"\u001b[36;1mWELCOME TO THE FITNESS CLI {user.name.upper()}!\u001b[0m")
    print("")
    print("")
    print("**************************")
    print("___________._____________________  ___________ _________ _________  _________ .____    .___ ")
    print("\_   _____/|   \__    ___/\      \ \_   _____//   _____//   _____/  \_   ___ \|    |   |   |")
    print(" |    __)  |   | |    |   /   |   \ |    __)_ \_____  \ \_____  \   /    \  \/|    |   |   |")
    print(" |     \   |   | |    |  /    |    \|        \/        \/        \  \     \___|    |___|   |")
    print(" \___  /   |___| |____|  \____|__  /_______  /_______  /_______  /   \______  /_______ \___|")
    print("     \/                          \/        \/        \/        \/          \/        \/    ")
    print("")
    print("✅ Create your own workout routines")
    print("✅ Create your own exercises")
    print("✅ Set your target number of reps and sets")
    print("✅ Assign exercises to your Workout Routines")
    print("")
    while True:
        print("   _____           __             _____                        ")
        print("  /     \  _____  |__| ____      /     \   ____   ____  __ __  ")      
        print(" /  \ /  \ \__  \ |  |/    \    /  \ /  \_/ __ \ /    \|  |  \ ")
        print("/    Y    \/ __  \|  |   |  \  /    Y    \  ___/|   |  \  |  / ")
        print("\____|__  (____  /__ |___|  /  \____|__  /\___  >___|  /____/  ")
        print("        \/     \/         \/           \/     \/     \/        ")
        menu()
        choice = input("> ").strip()
        if choice.lower() == 'wr':
            if not routines_list_with_menu():
                continue
        elif choice.lower() == 'e':
            if not exercises_list_with_menu():
                continue
        elif choice.lower() == 'x':
            exit_program()
        else:
            print(f'\u001b[41m{choice} is not valid. Please choose from the options below.\u001b[0m')

def menu():
    print("")
    print("**************************")
    print("")
    print("You are at the main menu. Choose from the options below.")
    print("")
    print(" >> Type WR or wr to view all WorkoutRoutines.")
    print(" >> Type E or e to view all Exercises.")
    print(" >> Type X or x to exit program.")
    print("")
    print("**************************")

def routines_list_with_menu():
    print("")
    print("\u001b[36;1mHere are all workout routines currently on record.\u001b[0m")
    print("")
    while True:
        routines = WorkoutRoutine.get_all()
        for i, routine in enumerate(routines, start=1):
            print(f'{i}.', routine.title)
        print("")
        routines_menu()
        choice = input("> ").strip()
        if choice.lower() =='r':
            return
        elif choice.lower() =='a':
            create_workout_routine()
            continue
        elif int(choice) in range(1, 100) and len(routines) >= int(choice):
            choice = int(choice)
            routine = routines[choice - 1]
            selected_routine(routine)
        elif choice.lower() =='x':
            exit_program()
        else:
            print(f'\u001b[41m{choice} is not valid. Please choose again.\u001b[0m')
            print("")
    return


def routines_menu():
        print("**************************")
        print("")
        print(" >>  Enter the workout routine number to view its details")
        print("     OR        ")
        print(" >>  Type A or a to add a new Workout Routine")
        print(" >>  Type R or r to return to the previous menu")
        print(" >>  Type X or x to exit program")
        print("")
        print("**************************")


def selected_routine(routine):
    while True:
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
        selected_routine_menu(routine)
        choice = input("> ")
        if choice.lower() =='e':
            edit_work_routine(routine)
            return
        elif choice.lower() =='d':
            confirmation = input("\u001b[43mDeleting this routine will delete all associated exercises.\u001b[0m\nDo you wish to continue? Y/N ")
            if choice.lower() =='y':
                delete_exercise(routine.exercises())
                delete_workout_routine(routine)
                return
            elif choice.lower() =='y':
                print(f"You have opted not to delete routine {id}.")
                print("")
                continue
            else:
                print(f'\u001b[41m{confirmation} is not a valid option. Please try again.\u001b[0m')
                print("")
                print("**************************")
                print("")
                selected_routine(id)
            return
        elif choice.lower() =='a':
            create_exercise(routine)
        elif choice.lower() == 'c':
            if len(routine.exercises()) == 1:
                terminate_exercise = routine.exercises()[0]
                confirmation = input(f'\u001b[43mAre you sure you want to delete {terminate_exercise.title}?\u001b[0m Y/N ')
                if confirmation.lower() == 'y':
                    delete_exercise([terminate_exercise])
                elif confirmation.lower() == 'n':
                    print("")
                    print("**************************")
                    print(f'You have opted not to delete the exercise.')
                    print("**************************")
                else:
                    print(f'\u001b[41m{confirmation} is not a valid exercise option. Please try again.\u001b[0m')
            else:
                selection = input(f'Which exercise do you wish to delete? ')
                if check_string(selection):
                    print('\u001b[41mYou will need to enter a numerical value that matches the exercise ID you wish to remove.\u001b[0m')
                else:
                    if int(selection) in range(1, 100) and len(routine.exercises()) >= int(selection):
                        confirmation = input(f'\u001b[43mAre you sure you want to delete exercise {selection}?\u001b[0m Y/N ')
                        breakpoint()
                        selection = int(selection) - 1
                        terminate_exercise = routine.exercises()[selection]
                        if confirmation.lower() == 'y':
                            print("")
                            print(f'\u001b[32;1m{terminate_exercise.title} has been deleted from routine {routine.title}\u001b[0m')
                            delete_exercise([terminate_exercise])
                        elif confirmation.lower() == 'n':
                            print("")
                            print("**************************")
                            print(f'You have opted not to delete {terminate_exercise.title}.')
                            print("**************************")
                        else:
                            print(f'\u001b[41m{selection} is not a valid option. Please try again.\u001b[0m')
                    else:
                        print('\u001b[41mYou will need to enter a numerical value that matches the exercise ID you wish to remove.\u001b[0m')
        elif choice.lower() == 'z':
            if len(routine.exercises()) == 1:
                exercise_to_edit = routine.exercises()[0]
                print("")
                print(f'\u001b[36;1mNow editing {exercise_to_edit.title}\u001b[0m')
                edit_exercise(exercise_to_edit)
            else:
                selection = input(f'Which exercise do you wish to edit? ')
                if check_string(selection):
                    print('\u001b[41mYou will need to enter a numerical value that matches the exercise you wish to edit.\u001b[0m')
                else: 
                    if int(selection) in range(1, 100) and len(routine.exercises()) >= int(selection):
                        selection = int(selection) - 1
                        exercise_to_edit = routine.exercises()[selection]
                        edit_exercise(exercise_to_edit, routine)
                    else:
                        print('\u001b[41mYou will need to enter a numerical value that matches the exercise number you wish to edit.\u001b[0m')
        elif choice.lower() == 'r':
            return
        elif choice.lower() == 'x':
            exit_program()
        else:
            print(f'\u001b[41m{choice} is not a valid option. Please try again.\u001b[0m')
    return


def selected_routine_menu(routine):
    print("**************************")
    print("")
    print(" >>  Type E or e to edit this workout routine")
    print(" >>  Type D or d to delete this workout routine")
    print(" >>  Type A or a to add a new exercise to workout routine")
    if routine.exercises():
        print(" >>  Type C or c to cut an exercise from this routine")
        print(" >>  Type Z or z to edit an exercise from this routine")
    print("     OR        ")
    print(" >>  Type R or r to return to the previous menu")
    # print(" >>  Type M to go back to main menu")
    print(" >>  Type X or x to exit program")
    print("")
    print("**************************")


def exercises_list_with_menu():
    while True:
        print("")
        print("\u001b[36;1mHere are all exercises currently on record.\u001b[0m")
        print("")
        exercises = Exercise.get_all()
        for i, exercise in enumerate(exercises, start = 1):
            print(f'{i}.', exercise.title)
        print("")
        exercises_list_menu()
        choice = input("> ").strip()
        if re.compile(r'^(?:[1-9]|[1-9]\d|100)$').match(choice) and len(exercises) >= int(choice):
            choice = int(choice)
            exercise = exercises[choice - 1]
            selected_exercise(exercise)
        elif re.compile(r'(?i)^a$').match(choice):
            create_exercise()
            continue
        elif re.compile(r'(?i)^r$').match(choice):
            return
        elif re.compile(r'(?i)^x$').match(choice):
            exit_program()
        else:
            print(f'\u001b[41m{choice} is not a valid option. Please try again.\u001b[0m')
    return

def exercises_list_menu():
    print("**************************")
    print("")
    print(" >>  Enter the exercise number to view its details")
    # print(" >>  Enter the exercise Name to view its details")
    print("     OR        ")
    print(" >>  Type A or a to add a new exercise")
    print(" >>  Type R or r to return to the previous menu")
    print(" >>  Type X or x to exit program")
    print("")
    print("**************************")

def selected_exercise(exercise):
    while True:
        print("")
        print(f'\u001b[36;1mYou are editing exercise {exercise.title}:\u001b[0m')
        print("")
        print(f'Exercise Title: {exercise.title}\nExercise Description: {exercise.description}\nTarget Reps: {exercise.reps}\nTarget Sets: {exercise.sets}')
        print("")
        routine = WorkoutRoutine.find_by_id(exercise.w_routine_id)
        selected_exercise_menu()
        choice = input("> ")
        if re.compile(r'(?i)^e$').match(choice):
            edit_exercise(exercise)
            continue
        elif re.compile(r'(?i)^d$').match(choice):
            decision = input(f'\u001b[43mAre you sure you want to delete {exercise.title}?\u001b[0m Y/N ')
            if re.compile(r'(?i)^y$').match(decision):
                print("")
                print(f'\u001b[32;1m{exercise.title} has been deleted.\u001b[0m')
                print("")
                delete_exercise([exercise])
            elif re.compile(r'(?i)^n$').match(decision):
                continue
            else:
                print("")
                print(f'\u001b[41m{decision} is not a valid option. Please try again.\u001b[0m')
            return
        elif re.compile(r'(?i)^v$').match(choice):
            routine = WorkoutRoutine.find_by_id(exercise.w_routine_id)
            print("")
            print(f'\u001b[36;1mHere are the details of the routine associated to this exercise:\u001b[0m')
            print(f'Routine Title: {routine.title}, Routine Equipment: {routine.equipment}')
            print("")
            decision = input(f'Would you like to edit {routine.title}? Y/N ')
            if re.compile(r'(?i)^y$').match(decision):
                edit_work_routine(routine, exercise)
            elif re.compile(r'(?i)^n$').match(decision):
                continue
            else:
                print("")
                print(f'\u001b[41m{decision} is not a valid option. Please try again.\u001b[0m')
                print("")
        elif re.compile(r'(?i)^r$').match(choice):
            return
        elif re.compile(r'(?i)^x$').match(choice):
            exit_program()
        else:
            print("")
            print(f'\u001b[41m{choice} is not a valid option. Please try again.\u001b[0m')
            print("")
    return
        
def selected_exercise_menu():
    print("**************************")
    print("")
    print(" >>  Type E or e to edit this exercise")
    print(" >>  Type D or d to Delete this exercise")
    print(" >>  Type V or v to view work routine details")
    print("     OR        ")
    print(" >>  Type R or r to return to the previous menu")
    print(" >>  Type X or x to exit program")
    print("")
    print("**************************")

if __name__ == "__main__":
    login()
