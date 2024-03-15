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

def exit_program():
    y_regex = re.compile(r'(?i)^y$')
    n_regex = re.compile(r'(?i)^n$')
    confirmation = input("\u001b[43mAre you sure you wish to exit?\u001b[0m Y/N ")
    if y_regex.match(confirmation):
        print("Goodbye!")
        exit()
    elif n_regex.match(confirmation):
        return
    else:
        print(f'\u001b[41m{confirmation} is not a valid option. Please try again.\u001b[0m')
        print("")
        print("**************************")
        print("")

def create_workout_routine():
    title = input(f'Enter the name of the new workout routine: ')
    equipment = input(f'Enter the equipment of the new routine: ')
    try:
        routine = WorkoutRoutine.create(title, equipment)
        print("")
        print(f'\u001b[32;1mSuccess! {routine.title} has been created!\u001b[0m')
        print("")
        print(routine)
        return
    except Exception as exc:
        print("\u001b[41mError creating workout routine:\u001b[0m ", exc)
    return


def edit_work_routine(id):
    if workout_routine := WorkoutRoutine.find_by_id(id):
        # breakpoint()
        if ex_id:
            print("")
            print("\u001b[36;1mChoose from the options below.\u001b[0m")
            print("")
            decision = input("  >>  Type T to update title:\n  >>  Type E to update equipment:\n  >>  Type B to update both:\n  >>  Type X to edit an exercise:\n\n**************************\n  >> ")
            if re.compile(r'(?i)^t$').match(decision):
                try:
                    title = input("Enter the workout routine's new title: ")
                    workout_routine.title = title
                    workout_routine.equipment = workout_routine.equipment
                    workout_routine.update()
                    print("")
                    print(f'\u001b[32;1mSuccess! {workout_routine.title} has been updated!\u001b[0m')
                except Exception as exc:
                    print("\u001b[41mError updating workout routine:\u001b[0m ", exc)
            elif re.compile(r'(?i)^e$').match(decision):
                try:
                    workout_routine.title = workout_routine.title
                    equipment = input("Enter the workout routine's new equipment: ")
                    workout_routine.equipment = equipment
                    workout_routine.update()
                    print("")
                    print(f'\u001b[32;1mSuccess! {workout_routine.title} has been updated!\u001b[0m')
                except Exception as exc:
                    print("\u001b[41mError updating workout routine:\u001b[0m ", exc)
            elif re.compile(r'(?i)^b$').match(decision):
                try:
                    title = input("Enter the workout routine's new title: ")
                    workout_routine.title = title
                    equipment = input("Enter the workout routine's new equipment: ")
                    workout_routine.equipment = equipment
                    workout_routine.update()
                    print("")
                    print(f'\u001b[32;1mSuccess! {workout_routine.title} has been updated!\u001b[0m')
                except Exception as exc:
                    print(f"\u001b[41m{exercise_id} is invalid. Please try again.\u001b[0m")
            elif re.compile(r'(?i)^x$').match(decision):
                exercise_id_regex = re.compile(r'^\d{1,3}$')
                exercise_id = input(f'Please select which exercise you want to edit: ')
                if exercise_id_regex.match(exercise_id):
                    if int(exercise_id) in ex_id:
                        exercise = Exercise.find_by_id(exercise_id)
                        print("")
                        print(f"You have opted to update exercise number {exercise.id}.")
                        print(exercise)
                        print("")
                        ###

                        t_regex = re.compile(r'(?i)^t$')
                        d_regex = re.compile(r'(?i)^d$')
                        r_regex = re.compile(r'(?i)^r$')
                        s_regex = re.compile(r'(?i)^s$')
                        w_regex = re.compile(r'(?i)^w$')
                        a_regex = re.compile(r'(?i)^a$')
                        prim_decision = input("What would you like to update?\nType T for title:\nType D for description:\nType R for reps:\nType S for sets:\nType W for workout routine id:\nType A for all:\n\n**************************\n  >> ")
                        if t_regex.match(prim_decision):
                            try:
                                title = input("Enter the exercises new title: ")
                                exercise.title = title
                                exercise.description = exercise.description
                                exercise.reps = exercise.reps
                                exercise.sets = exercise.sets
                                exercise.w_routine_id = exercise.w_routine_id
                                print("")
                                print(f'\u001b[32;1mSuccess! Title for exercise number {exercise.id} has been updated.\u001b[0m')
                                print("")
                                exercise.update()
                            except Exception as exc:
                                print("\u001b[41mError updating exercise:\u001b[0m ", exc)
                        elif d_regex.match(prim_decision):
                            try:
                                exercise.title = exercise.title
                                description = input("Enter the exercises new description: ")
                                exercise.description = description
                                exercise.reps = exercise.reps
                                exercise.sets = exercise.sets
                                exercise.w_routine_id = exercise.w_routine_id
                                print("")
                                print(f'\u001b[32;1mSuccess! Description for exercise number {exercise.id} has been updated.\u001b[0m')
                                print("")
                                exercise.update()
                            except Exception as exc:
                                print("\u001b[41mError updating exercise:\u001b[0m ", exc)
                        elif r_regex.match(prim_decision):
                            try:
                                exercise.title = exercise.title
                                exercise.description = exercise.description
                                reps = input("Enter the updated number of reps: ")
                                exercise.reps = int(reps)
                                exercise.sets = exercise.sets
                                exercise.w_routine_id = exercise.w_routine_id
                                print("")
                                print(f'\u001b[32;1mSuccess! Reps for exercise number {exercise.id} has been updated.\u001b[0m')
                                print("")
                                exercise.update()
                            except Exception as exc:
                                print("\u001b[41mError updating exercise:\u001b[0m ", exc)
                        elif s_regex.match(prim_decision):
                            try:
                                exercise.title = exercise.title
                                exercise.description = exercise.description
                                exercise.reps = exercise.reps
                                sets = input("Enter the updated number of sets: ")
                                exercise.sets = int(sets)
                                exercise.w_routine_id = exercise.w_routine_id
                                print("")
                                print(f'\u001b[32;1mSuccess! Sets for exercise number {exercise.id} has been updated.\u001b[0m')
                                print("")
                                exercise.update()
                            except Exception as exc:
                                print("\u001b[41mError updating exercise:\u001b[0m ", exc)
                        elif w_regex.match(prim_decision):
                            try:
                                exercise.title = exercise.title
                                exercise.description = exercise.description
                                exercise.reps = exercise.reps
                                exercise.sets = exercise.sets
                                new_regex = re.compile(r'(?i)^n$')
                                exist_regex = re.compile(r'(?i)^e$')
                                print("")
                                decision = input(f'Would you like to create a new Workout Routine for this exercise or assign to an existing?\n  >>  Type N for New | Type E for Exisiting: ')
                                print("")
                                if new_regex.match(decision):
                                    print("You have opted to create a new workout routine.")
                                    print("")
                                    wr_title = input('Enter new workout routine title: ')
                                    wr_equipment = input('Enter new workout routine equipment: ')
                                    try:
                                        new_wr = WorkoutRoutine.create(wr_title, wr_equipment)
                                        wr = WorkoutRoutine.get_all()
                                        w_routine_id = int(new_wr.id)
                                        exercise.w_routine_id = w_routine_id
                                        # breakpoint()
                                        print("")
                                        print(f'\u001b[32;1mSuccess! {exercise.title.upper()} is now associated to your new workout routine, {new_wr.title.upper()}, ID number {new_wr.id}.\u001b[0m')
                                        exercise.update()
                                    except Exeption as exc:
                                        print("\u001b[41mError updating exercise:\u001b[0m ", exc)
                                elif exist_regex.match(decision):
                                    wo = WorkoutRoutine.get_all()
                                    print(f'\u001b[36;1mCurrent Workout Routines in database:\u001b[0m')
                                    for wos in wo:
                                        print(f'ID: {wos.id},Title: {wos.title}')
                                    w_routine_id_regex = re.compile(r'^\d{1,3}$')
                                    w_routine_id = input(f'Enter the workout routine id number you wish to apply this exercise: ')
                                    exercise.w_routine_id = int(w_routine_id)
                                    # breakpoint()
                                    if w_routine_id_regex.match(w_routine_id):
                                        print("")
                                        print(f'\u001b[32;1mSuccess! Exercise number {exercise.id} is now associated to workout routine number {exercise.w_routine_id}!\u001b[0m')
                                        exercise.update()
                                        print(exercise)
                                    else:
                                        print("")
                                        print("\u001b[41mPlease enter a valid workout routine id number.\u001b[0m")
                                        print("")
                                else:
                                    print("")
                                    print(f"\u001b[41m{decision} is invalid. Please try again.\u001b[0m")
                                    print("")
                            except Exception as exc:
                                print("\u001b[41mError updating exercise:\u001b[0m ", exc)
                        elif a_regex.match(prim_decision):
                            try:
                                title = input("Enter the exercises new title: ")
                                exercise.title = title
                                description = input("Enter the exercises new description: ")
                                exercise.description = description
                                reps = input("Enter the new number of reps for this exercise: ")
                                exercise.reps = int(reps)
                                sets = input("Enter the new number of sets for this exercise: ")
                                exercise.sets = int(sets)
                                new_regex = re.compile(r'(?i)^n$')
                                exist_regex = re.compile(r'(?i)^e$')
                                print("")
                                decision = input(f'Would you like to create a new Workout Routine for this exercise or assign to an existing?\n  >>  Type N for New | Type E for Exisiting: ')
                                print("")
                                if new_regex.match(decision):
                                    print("You have opted to create a new workout routine.")
                                    print("")
                                    wr_title = input('Enter new workout routine title: ')
                                    wr_equipment = input('Enter new workout routine equipment: ')
                                    try:
                                        new_wr = WorkoutRoutine.create(wr_title, wr_equipment)
                                        wr = WorkoutRoutine.get_all()
                                        w_routine_id = wr[-1].id
                                        print("")
                                        print(f'\u001b[32;1mSuccess! {exercise.title} is now associated to your new workout routine, {new_wr.title}\u001b[0m')
                                        print(exercise)
                                        exercise.update()
                                    except Exeption as exc:
                                        print("\u001b[41mError updating exercise:\u001b[0m ", exc)
                                elif exist_regex.match(decision):
                                    wo = WorkoutRoutine.get_all()
                                    print(f'\u001b[36;1mCurrent Workout Routines in database:\u001b[0m')
                                    for wos in wo:
                                        print(f'ID: {wos.id},Title: {wos.title}')
                                    w_routine_id_regex = re.compile(r'^\d{1,3}$')
                                    w_routine_id = input(f'Enter the workout routine id number you wish to apply this exercise: ')
                                    exercise.w_routine_id = int(w_routine_id)
                                    # breakpoint()
                                    if w_routine_id_regex.match(w_routine_id):
                                        print("")
                                        print(f'\u001b[32;1mSuccess! Exercise number {exercise.id} is now associated to workout routine {w_routine_id}!\u001b[0m')
                                        print(exercise)
                                        exercise.update()
                                    else:
                                        print("")
                                        print("\u001b[41mPlease enter a valid workout routine id number.\u001b[0m")
                                        print("")
                                else:
                                    print("")
                                    print(f"\u001b[41m{decision} is invalid. Please try again.\u001b[0m")
                                    print("")
                            except Exception as exc:
                                print("\u001b[41mError updating exercise:\u001b[0m ", exc)
                        else:
                            print(f'\u001b[41mThat is not a valid option. Please try again.\u001b[0m')
                    else:
                        print(f'\u001b[41m{exercise_id} is invalid. Please try again.\u001b[0m')
                ###
                else:
                    print(f"\u001b[41m{exercise_id} is invalid. Please try again.\u001b[0m")
            else:
                print(f'\u001b[41m{decision} is invalid. Please try again.\u001b[0m')
        else:
            decision = input("  >>  Type T to update title:\n  >>  Type E to update equipment:\n  >>  Type B to update both:\n**************************\n  >> ")
            if t_regex.match(decision):
                try:
                    title = input("Enter the workout routine's new title: ")
                    workout_routine.title = title
                    workout_routine.equipment = workout_routine.equipment
                    workout_routine.update()
                    print("")
                    print(f'\u001b[32;1mSuccess! {workout_routine.title} has been updated!\u001b[0m')
                except Exception as exc:
                    print("\u001b[41mError updating workout routine:\u001b[0m ", exc)
            elif e_regex.match(decision):
                try:
                    workout_routine.title = workout_routine.title
                    equipment = input("Enter the workout routine's new equipment: ")
                    workout_routine.equipment = equipment
                    workout_routine.update()
                    print("")
                    print(f'\u001b[32;1mSuccess! {workout_routine.title} has been updated!\u001b[0m')
                except Exception as exc:
                    print("\u001b[41mError updating workout routine:\u001b[0m ", exc)
            elif b_regex.match(decision):
                try:
                    title = input("Enter the workout routine's new title: ")
                    workout_routine.title = title
                    equipment = input("Enter the workout routine's new equipment: ")
                    workout_routine.equipment = equipment
                    workout_routine.update()
                    print("")
                    print(f'\u001b[32;1mSuccess! {workout_routine.title} has been updated!\u001b[0m')
                except Exception as exc:
                    print("\u001b[41mError updating workout routine:\u001b[0m ", exc)
            else:
                print(f'\u001b[41m{decision} is invalid. Please try again.\u001b[0m')
    else:
        print(f'\u001b[41mWorkout Routine {id} not found.\u001b[0m')
    wo_r = WorkoutRoutine.find_by_id(id)
    print("")
    print(f'You are still editing workout routine number {wo_r.id}')
    print(wo_r)
    wr_choice_options(id)