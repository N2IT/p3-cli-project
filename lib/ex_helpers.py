import os
import re
from models.workout_routine import WorkoutRoutine
from models.exercise import Exercise 

def list_exercises_w_menu():
    exercise = Exercise.get_all()
    ex_id = []
    print("")
    print("Here are all exercises currently on record.")
    print("")
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
            from wr_helpers import exit_program
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
                ex_delete_exercise(id)
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
            exercise = Exercise.get_all()
            for exercises in exercise:
                print(f'ID: {exercises.id}, Title: {exercises.title}')
            return
        elif x_regex.match(choice):
            from wr_helpers import exit_program
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
    if exercise := Exercise.find_by_id(id):
        try:
            title = input("Enter the exercises new title: ")
            exercise.title = title
            description = input("Enter the exercises new description: ")
            exercise.description = description
            reps = input("Enter the new number of reps for this exercise: ")
            exercise.reps = int(reps)
            sets = input("Enter the new number of sets for this exercise: ")
            exercise.sets = int(sets)
            wo = WorkoutRoutine.get_all()
            print(f'Current Workout Routines in database:')
            for wos in wo:
                print(f'ID: {wos.id},Title: {wos.title}')
            w_routine_id_regex = re.compile(r'^\d{1,3}$')
            w_routine_id = input(f'Enter the new workout routine id number you wish to apply this exercise: ')
            if w_routine_id_regex.match(w_routine_id):
                exercise.w_routine_id = w_routine_id
                print("")
                print(f'Success! Exercise number {exercise.id} has been updated!')
                print(exercise)
                exercise.update()
                return
            else:
                print("")
                print("Please enter a valid workout routine id number.")
                print("")
        except Exception as exc:
            print("Error updating exercise: ", exc)
    else:
        print(f'Workout Routine {id} not found.')
            
def ex_delete_exercise(id):
    if exercise := Exercise.find_by_id(id):
        exercise.delete()
        print("")
        print(f'Exercise {id} has been deleted.')
        print("")
    
    exercises = Exercise.get_all()
    for exercises in exercises:
        print(f'ID: {exercises.id}, Title: {exercises.title}')

def create_exercise():
    title = input('Enter a title for your exercise: ')
    description = input('Enter a description of your exercise: ')
    reps = input('Enter the target number of reps for your exercise: ')
    sets = input('Enter the target number of sets for your exercise: ')
    print('You will need to assign this exercise to a workout routine.')
    new_regex = re.compile(r'(?i)^n$')
    exist_regex = re.compile(r'(?i)^e$')
    decision = input(f'Would you like to create a new Workout Routine for this exercise or assign to an existing?\nType N for New | Type E for Exisiting: ')
    if new_regex.match(decision):
        wr_title = input('Enter new workout routine title: ')
        wr_equipment = input('Enter new workout routine equipment: ')
        try:
            new_wr = WorkoutRoutine.create(wr_title, wr_equipment)
            wr = WorkoutRoutine.get_all()
            w_routine_id = wr[-1].id
            new_exercise = Exercise.create(title, description, int(reps), int(sets), int(w_routine_id))
            print("")
                print(f'Success! {exercise.title} has been created.')
                print("")
        except Exception as exc:
            print("")
            print("Error creating exercise: ", exc)
            print("")
    elif exist_regex.match(decision):
        wo = WorkoutRoutine.get_all()
        print(f'Current Workout Routines in database:')
        for wos in wo:
            print(f'ID: {wos.id},Title: {wos.title}')
        w_routine_id_regex = re.compile(r'^\d{1,3}$')
        w_routine_id = input(f'Enter the workout routine id number you wish to apply this exercise: ')
        if w_routine_id_regex.match(w_routine_id):
            try:
                exercise = Exercise.create(title, description, int(reps), int(sets), int(w_routine_id))
                print("")
                print(f'Success! {exercise.title} has been created.')
                print("")
            except Exception as exc:
                print("")
                print("Error creating exercise: ", exc)
                print("")
        else: 
            print("")
            print("Please enter a valid workout routine id number.")
            print("")
    else:
        print(f'{decision} is not a valid option. Please try again.')
    exos = Exercise.get_all()
    latest_exer = exos[-1]
    print(latest_exer)
    ex_choice_options(latest_exer.id)
    
