# lib/cli.py
import re
import time
from models.user import User
from models.workout_routine import WorkoutRoutine
from models.exercise import Exercise 
from helpers import (
    print_invalid_choice,
    validate_integer_input,
    check_string,
    print_exercises_list,
    return_exercises,
    exercise_number_selected_from_menu,
    print_routines_list,
    return_routines,
    print_selected_exercise,
    exercise_menu_option_d,
    exercise_menu_option_v,
    routine_menu_option_d,
    routine_number_selected_from_menu,
    clear_screen,
    exit_program,
    create_workout_routine,
    edit_work_routine,
    delete_workout_routine,
    edit_exercise,
    create_exercise,
    delete_exercise
)

def login():
    clear_screen()
    name = input("Please enter your name: ")
    try:
        user = User.create(name)
        main(user)
    except Exception as exc:
        print("\u001b[41mError creating user:\u001b[0m ", exc)
    
def main(user=None):
    clear_screen()
    print("")
    print(f"\u001b[36;1mWELCOME TO THE FITNESS CLI {user.name}!\u001b[0m")
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
            print_invalid_choice(choice)
    return

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



## LIST OF ROUTINES AND RELATED MENU ##

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

def routines_list_with_menu():
    while True:
        print_routines_list()
        routines_menu()
        choice = input("> ").strip()
        if check_string(choice):
            if choice.lower() =='r':
                return
            elif choice.lower() =='a':
                create_workout_routine()
                continue
            elif choice.lower() == 'x':
                exit_program()
            else:
                print_invalid_choice(choice)
        else:
            routine_number_selected_from_menu(choice)
    return



## SELECTED ROUTINE AND RELATED MENU ##

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
            routine_menu_option_d(routine)
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
                    print(f'You have opted not to delete {terminate_exercise.title}.')
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


## LIST OF ROUTINES AND RELATED MENU ##

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


def exercises_list_with_menu():
    while True:
        print_exercises_list()
        return_exercises()
        exercises_list_menu()
        choice = input("> ").strip()
        if check_string(choice):
            if choice.lower() == 'a':
                create_exercise()
                continue
            elif choice.lower() == 'r':
                return
            elif choice.lower() == 'x':
                exit_program()
            else:
                print_invalid_choice(choice)
        else: 
            exercise_number_selected_from_menu(choice)
    return

## SELECTED ROUTINE AND RELATED MENU ##

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


def selected_exercise(exercise):
    while True:
        print_selected_exercise(exercise)
        routine = WorkoutRoutine.find_by_id(exercise.w_routine_id)
        selected_exercise_menu()
        choice = input("> ")
        if choice.lower() == 'e':
            edit_exercise(exercise)
        elif choice.lower() == 'd':
            exercise_menu_option_d(exercise)
            return
        elif choice.lower() == 'v':
            exercise_menu_option_v(routine, exercise)
        elif choice.lower() == 'r':
            return
        elif choice.lower() == 'x':
            exit_program()
        else:
            print_invalid_choice(choice)
    return
        

if __name__ == "__main__":
    login()
