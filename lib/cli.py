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


def countdown_timer_routines(seconds, routine):
    while seconds > 0:
        if seconds == 1:
            print(f'Passing you over to edit in \u001b[33m{seconds}\u001b[0m second', end='\r')
        elif seconds == 2 or seconds == 3:
            print(f'Passing you over to edit in \u001b[31m{seconds}\u001b[0m seconds', end='\r')
        time.sleep(1)
        seconds -= 1
    edit_work_routine(routine)

def countdown_timer_exercises(seconds, exercise):
    while seconds > 0:
        if seconds == 1:
            print(f'Passing you over to edit in \u001b[33m{seconds}\u001b[0m second', end='\r')
        elif seconds == 2 or seconds == 3:
            print(f'Passing you over to edit in \u001b[31m{seconds}\u001b[0m seconds', end='\r')
        time.sleep(1)
        seconds -= 1
    edit_exercise(exercise)

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
    print("___________._____________________  ___________ _________ _________ _________ .____    .___ ")
    print("\_   _____/|   \__    ___/\      \ \_   _____//   _____//   _____/ \_   ___ \|    |   |   |")
    print(" |    __)  |   | |    |   /   |   \ |    __)_ \_____  \ \_____  \  /    \  \/|    |   |   |")
    print(" |     \   |   | |    |  /    |    \|        \/        \/        \ \     \___|    |___|   |")
    print(" \___  /   |___| |____|  \____|__  /_______  /_______  /_______  /  \______  /_______ \___|")
    print("     \/                          \/        \/        \/        \/          \/        \/    ")
    print("")
    print("✅ Create your own workout routines")
    print("✅ Create your own exercises")
    print("✅ Set your target number of reps and sets")
    print("✅ Assign exercises to your Workout Routines")
    print("")
    while True:
        menu()
        choice = input("> ").strip()
        if re.compile(r'(?i)^wR$').match(choice):
            if not list_workout_routines_w_menu():
                continue
        elif re.compile(r'(?i)^e$').match(choice):
            if not list_exercises_w_menu():
                continue
        elif re.compile(r'(?i)^x$').match(choice):
            exit_program()
        else:
            print(f'\u001b[41m{choice} is not valid. Please choose from the options below.\u001b[0m')


def menu():
    print("")
    print("**************************")
    print("")
    print("You are at the main menu. Choose from the options below.")
    print("")
    print(" >> Type WR to view all WorkoutRoutines.")
    print(" >> Type E to view all Exercises.")
    print(" >> Type X to exit program.")
    print("")
    print("**************************")

        
def list_workout_routines_w_menu():
    print("")
    print("\u001b[36;1mHere are all workout routines currently on record.\u001b[0m")
    print("")
    while True:
        routines = WorkoutRoutine.get_all()
        for i, routine in enumerate(routines, start=1):
            print(f'{i}.', routine.title)
        print("")
        wr_menu_options()
        choice = input("> ").strip()
        if re.compile(r'(?i)^r$').match(choice):
            return
        elif re.compile(r'(?i)^a$').match(choice):
            create_workout_routine()
            continue
        elif re.compile(r'^[1-9]$').match(choice) and len(routines) >= int(choice):
            breakpoint()
            choice = int(choice)
            routine = routines[choice - 1]
            wr_choice_options(routine)
        elif re.compile(r'(?i)^x$').match(choice):
            exit_program()
        else:
            print(f'\u001b[41m{choice} is not valid. Please choose again.\u001b[0m')
            print("")
    return


def wr_menu_options():
        print("**************************")
        print("")
        print(" >>  Enter the workout routine number to view its details")
        print("     OR        ")
        print(" >>  Type A to add a new Workout Routine")
        print(" >>  Type R to return to the previous menu")
        print(" >>  Type X to exit program")
        print("")
        print("**************************")


def wr_choice_options(routine):
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
        wr_choice_options_menu(routine)
        choice = input("> ")
        if re.compile(r'(?i)^e$').match(choice):
            edit_work_routine(routine)
            return
        elif re.compile(r'(?i)^a$').match(choice):
            create_exercise(routine)
        elif re.compile(r'(?i)^c$').match(choice):
            selection = input(f'Which exercise do you wish to delete? ')
            if re.compile(r'^[1-9]$').match(selection):
                confirmation = input(f'\u001b[43mAre you sure you want to delete exercise {selection}?\u001b[0m Y/N ')
                selection = int(selection) - 1
                terminate_exercise = routine.exercises()[selection]
                if re.compile(r'(?i)^y$').match(confirmation):
                    print("")
                    print(f'\u001b[32;1m{terminate_exercise.title} has been deleted from routine {routine.title}\u001b[0m')
                    delete_exercise([terminate_exercise])
                elif re.compile(r'(?i)^n$').match(confirmation):
                    print("")
                    print("**************************")
                    print(f'You have opted not to delete {terminate_exercise.title}.')
                    print("**************************")
                else:
                    print(f'\u001b[41m{selection} is not a valid exercise option. Please try again.\u001b[0m')
            else:
                print('\u001b[41mYou will need to enter a numerical value that matches the exercise ID you wish to remove.\u001b[0m')
        elif re.compile(r'(?i)^d$').match(choice):
            confirmation = input("\u001b[43mDeleting this routine will delete all associated exercises.\u001b[0m\nDo you wish to continue? Y/N ")
            if re.compile(r'(?i)^y$').match(confirmation):
                delete_exercise(routine.exercises())
                delete_workout_routine(routine)
                return
            elif re.compile(r'(?i)^n$').match(confirmation):
                print(f"You have opted not to delete routine {id}.")
                print("")
                continue
            else:
                print(f'\u001b[41m{confirmation} is not a valid option. Please try again.\u001b[0m')
                print("")
                print("**************************")
                print("")
                wr_choice_options(id)
            return
        elif re.compile(r'(?i)^r$').match(choice):
            return
        elif re.compile(r'(?i)^x$').match(choice):
            exit_program()
        else:
            print(f'\u001b[41m{choice} is not a valid option. Please try again.\u001b[0m')
    return


def wr_choice_options_menu(routine):
    print("**************************")
    print("")
    print(" >>  Type E to edit this workout routine")
    print(" >>  Type A to add a new exercise to workout routine")
    if routine.exercises():
        print(" >>  Type C to cut an exercise from workout routine")
    print(" >>  Type D to delete this workout routine")
    print("     OR        ")
    print(" >>  Type R to return to the previous menu")
    # print(" >>  Type M to go back to main menu")
    print(" >>  Type X to exit program")
    print("")
    print("**************************")


def list_exercises_w_menu():
    while True:
        print("")
        print("\u001b[36;1mHere are all exercises currently on record.\u001b[0m")
        print("")
        WorkoutRoutine.get_all()
        exercises = Exercise.get_all()
        routines = WorkoutRoutine.all
        for i, exercise in enumerate(exercises, start = 1):
            print(f'{i}.', exercise.title)
        print("")
        ex_list_menu()
        choice = input("> ").strip()
        if re.compile(r'^[1-9]$').match(choice) and len(exercises) >= int(choice):
            print("")
            print(f"\u001b[36;1mHere are exercise {choice}'s details:\u001b[0m")
            print("")
            choice = int(choice)
            exercise = exercises[choice - 1]
            routine = WorkoutRoutine.find_by_id(exercise.w_routine_id)
            print(f'Exercise Title: {exercise.title}\nExercise Description: {exercise.description}\nTarget Reps: {exercise.reps}\nTarget Sets: {exercise.sets}\nRoutine {routine.title}, Equipment {routine.equipment}')
            ex_choice_options(exercise, routine)
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


def ex_list_menu():
    print("**************************")
    print("")
    print(" >>  Enter the exercise ID to view its details")
    # print(" >>  Enter the exercise Name to view its details")
    print("     OR        ")
    print(" >>  Type A to add a new exercise")
    print(" >>  Type R to return to the previous menu")
    print(" >>  Type X to exit program")
    print("")
    print("**************************")


def ex_choice_options(exercise, routine):
    while True:
        ex_choice_options_menu()
        choice = input("> ")
        if re.compile(r'(?i)^e$').match(choice):
            edit_exercise(exercise)
            continue
        elif re.compile(r'(?i)^d$').match(choice):
            delete_exercise([exercise])
            continue
        elif re.compile(r'(?i)^v$').match(choice):
            print("")
            print(f'\u001b[36;1mHere are the details of the routine associated to this exercise:\u001b[0m')
            print(f'Routine Title: {routine.title}, Routine Equipment: {routine.equipment}')
            print("")
            decision = input(f'Would you like to edit {routine.title}? Y/N ')
            if re.compile(r'(?i)^y$').match(decision):
                seconds = 3
                countdown_timer_routines(seconds, routine)
            elif re.compile(r'(?i)^y$').match(decision):
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
        

def ex_choice_options_menu():
    print("**************************")
    print("")
    print(" >>  Type E to edit this exercise")
    print(" >>  Type D to Delete this exercise")
    print(" >>  Type V to view work routine details")
    print("     OR        ")
    print(" >>  Type R to return to the previous menu")
    print(" >>  Type X to exit program")
    print("")
    print("**************************")


if __name__ == "__main__":
    login()
