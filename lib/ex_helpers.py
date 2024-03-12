import os
import re
from models.workout_routine import WorkoutRoutine
from models.exercise import Exercise 

def list_exercises_w_menu():
    exercise = Exercise.get_all()
    print("")
    print("Here are all the exercises currently in the database.")
    print("")
    ex_id = []
    for exercises in exercise:
        print(f'ID: {exercises.id}, Title: {exercises.title}')
        ex_id.append(str(exercises.id))
    while True:
        ex_menu_options()
        choice = input("> ").strip()
        ret_choice_regex = re.compile(r'(?i)^r$')
        add_choice_regex = re.compile(r'(?i)^a$')
        x_regex = re.compile(r'(?i)^x$')
        if ret_choice_regex.match(choice):
            return
        elif add_choice_regex.match(choice):
            create_exercise()
            continue
        elif choice in ex_id:
            choice = int(choice)
            ex = Exercise.find_by_id(choice)
            if ex:
                # clear_screen()
                print("")
                print(f"Here are the details for exercise {choice}:")
                print("")
                print(ex)
            else: 
                print(f'Exercise {choice} not found')
            ex_choice_options(choice)
        elif x_regex.match(choice):
            exit_program()
        else:
            print(f'{choice} is not valid. Please choose again.')
    return False

def ex_menu_options():
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

def create_exercise():
    pass

def ex_choice_options(id):
    while True:
        ex_choice_options_menu()
        exer = Exercise.find_by_id(id)
        choice = input("> ")
        ex_edit_regex = re.compile(r'(?i)^e$')
        ex_delete_regex = re.compile(r'(?i)^d$')
        prv_menu_regex = re.compile(r'(?i)^r$')
        x_regex = re.compile(r'(?i)^x$')
        y_regex = re.compile(r'(?i)^y$')
        n_regex = re.compile(r'(?i)^n$')
        if ex_edit_regex.match(choice):
            edit_exercise(id)
            continue
        elif ex_delete_regex.match(choice):
            confirmation = input("Do you wish to delete this exercise? Y/N ")
            if y_regex.match(confirmation):
                wr_delete_exercises(id)
                return
            elif n_regex.match(confirmation):
                print(f"You have opted not to delete exercise {id}.")
                print("")
                continue
            else:
                print(f'{confirmation} is not a valid option. Please try again.')
                print("")
                print("**************************")
                print("")
                ex_choice_options(id)
            return
        elif prv_menu_regex.match(choice):
            return
        elif x_regex.match(choice):
            exit_program()
        else:
            print(f'{choice} is not a valid option. Please try again.')
            print("")
            print("**************************")
            print("")

def ex_choice_options_menu():
    print("**************************")
    print("")
    print(" >>  Type E to edit this exercise")
    print(" >>  Type D to Delete this workout routine")
    print("                     OR                      ")
    print(" >>  Type R to return to the previous menu")
    print(" >>  Type X to exit program")
    print("")
    print("**************************")

def edit_exercise(id):
    pass

def delete_exercise(id):
    pass

