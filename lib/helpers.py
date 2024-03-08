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
    
def list_workout_routines():
    workout_routines = WorkoutRoutine.get_all()
    clear_screen()
    print("")
    print("Here are all workout routines currently on record.")
    print("")
    wo_id = []
    for workout_routine in workout_routines:
        print(f'ID: {workout_routine.id}, Title: {workout_routine.title}')
        wo_id.append(str(workout_routine.id))
    while True:
        wr_options()
        choice = input("> ").strip()
        ret_choice_regex = re.compile(r'(?i)^r$')
        add_choice_regex = re.compile(r'(?i)^a$')
        if ret_choice_regex.match(choice):
            from cli import menu
            menu()
            return False
        elif add_choice_regex.match(choice):
            create_workout_routine()
        elif choice in wo_id:
            choice = int(choice)
            wo_r = WorkoutRoutine.find_by_id(choice)
            exercise = Exercise.get_all()
            if wo_r:
                clear_screen()
                print("")
                print(f"Here are the workout routine {choice} details.")
                print("")
                print(wo_r)
            else: 
                print(f'Workout Routine {choice} not found')
            for exercises in exercise:
                if exercises.w_routine_id == int(choice):
                    print(f'    {exercises}')
            wr_choice_options(choice)
        else:
            print(f'{choice} is not valid. Please choose again.')

def wr_options():
    print("**************************")
    print("")
    print(" >>  Enter the workout routine id to view its details")
    print("                     OR                      ")
    print(" >>  Type A to add a new Workout Routine")
    print(" >>  Type R to return to the previous menu")
    print("")
    print("**************************")

def wr_choice_options(id):
    while True:
        wr_choice_options_menu()
        choice = input("> ")
        wor_edit_regex = re.compile(r'(?i)^e$')
        wor_add_exercise_regex = re.compile(r'(?i)^a$')
        wor_delete_regex = re.compile(r'(?i)^d$')
        prv_menu_regex = re.compile(r'(?i)^r$')
        m_menu_regex = re.compile(r'(?i)^m$')
        x_regex = re.compile(r'(?i)^x$')
        if wor_edit_regex.match(choice):
            edit_work_routine(id)
        elif wor_add_exercise_regex.match(choice):
            wor_add_exercise(id)
        elif wor_delete_regex.match(choice):
            delete_workout_routine(id)
        elif prv_menu_regex.match(choice):
            list_workout_routines()
        # elif m_menu_regex.match(choice):
        #     from cli import menu
        #     clear_screen()
        #     menu()
        #     return False
        elif x_regex.match(choice):
            exit_program()

def wr_choice_options_menu():
    print("**************************")
    print("")
    print(" >>  Type E to edit this workout routine")
    print(" >>  Type A to add a new exercise to workout routine")
    print(" >>  Type D to Delete this workout routine")
    print("                     OR                      ")
    print(" >>  Type R to return to the previous menu")
    # print(" >>  Type M to go back to main menu")
    print(" >>  Type X to exit program")
    print("")
    print("**************************")

def edit_work_routine(id):
    if workout_routine := WorkoutRoutine.find_by_id(id):
        try:
            title = input("Enter the workout routine's new title: ")
            workout_routine.title = title
            equipment = input("Enter the workout routine's equipment: ")
            workout_routine.equipment = equipment
            workout_routine.update()
            print("")
            print(f'Success! {workout_routine.title} has been updated!')
        except Exception as exc:
            print("Error updating workout routine: ", exc)
    else:
        print(f'Workout Routine {id} not found.')

    
def wor_add_exercise(id):
    title = input(f'Enter new exercise title: ')
    description = input(f'Enter new exercise description: ')
    reps = input(f'Enter target number of reps for new exercise: ')
    sets = input(f'Enter target number of sets for new exercise: ')
    w_routine_id = id
    try:
        exercise = Exercise.create(title, description, int(reps), int(sets), w_routine_id)
        print(f'Success! {exercise.title} has been created!')
        print("")
    except Exception as exc:
        print("Error creating exercise: ", exc)

def delete_workout_routine():
    pass

def create_workout_routine():
    print('workout routine added!')


def list_exercises():
    pass
    
def exit_program():
    confirmation = input("Are you sure you wish to exit? Y/N ")
    if confirmation == "Y" or confirmation == "y":
        print("Goodbye!")
        exit()
    elif confirmation == "N" or confirmation == "n":
        return None
    else:
        print(f'{confirmation} is not a valid option. Please try again.')
        print("")
        print("**************************")
        print("")
        exit_program()

# def menu():
#     choice = input("> ")
