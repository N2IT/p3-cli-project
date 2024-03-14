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


def wr_list_exercises(id):
    exercises = Exercise.get_all()
    for exercise in exercises:
        if exercise.w_routine_id == id:
            print(f'    {exercise}')
    return


def list_workout_routines_w_menu():
    wo_id = []
    while True:
        print("")
        print("\u001b[36;1mHere are all workout routines currently on record.\u001b[0m")
        print("")
        workout_routines = WorkoutRoutine.get_all()
        for workout_routine in workout_routines:
            print(f'ID: {workout_routine.id}, Title: {workout_routine.title}')
            wo_id.append(str(workout_routine.id))
        wr_menu_options()
        choice = input("> ").strip()
        ret_choice_regex = re.compile(r'(?i)^r$')
        add_choice_regex = re.compile(r'(?i)^a$')
        x_regex = re.compile(r'(?i)^x$')
        if ret_choice_regex.match(choice):
            return
        elif add_choice_regex.match(choice):
            create_workout_routine()
            continue
        elif choice in wo_id:
            choice = int(choice)
            wo_r = WorkoutRoutine.find_by_id(choice)
            exercise = Exercise.get_all()
            if wo_r:
                # clear_screen()
                print("")
                print(f"\u001b[36;1mHere are the workout routine {choice} details.\u001b[0m")
                print("")
                print(wo_r)
            else: 
                print(f'\u001b[41mWorkout Routine {choice} not found\u001b[0m')
            for exercises in exercise:
                if exercises.w_routine_id == int(choice):
                    print(f'    {exercises}')
            wr_choice_options(choice)
        elif x_regex.match(choice):
            exit_program()
        else:
            print(f'\u001b[41m{choice} is not valid. Please choose again.\u001b[0m')
    return

def wr_menu_options():
    print("**************************")
    print("")
    print(" >>  Enter the workout routine ID to view its details")
    print("     OR        ")
    print(" >>  Type A to add a new Workout Routine")
    print(" >>  Type R to return to the previous menu")
    print(" >>  Type X to exit program")
    print("")
    print("**************************")


def wr_choice_options(id):
    exercise_id = []
    while True:
        exercise = Exercise.get_all()
        for exos in exercise:
            if exos.w_routine_id == id:
                exercise_id.append(exos.id)
        if exercise_id:
            wr_choice_options_menu_w_cut()
        else:
            wr_choice_options_menu()
        routine = WorkoutRoutine.find_by_id(id)
        choice = input("> ")
        wr_edit_regex = re.compile(r'(?i)^e$')
        wr_add_exercise_regex = re.compile(r'(?i)^a$')
        wr_cut_exercise_regex = re.compile(r'(?i)^c$')
        wr_delete_regex = re.compile(r'(?i)^d$')
        prv_menu_regex = re.compile(r'(?i)^r$')
        x_regex = re.compile(r'(?i)^x$')
        y_regex = re.compile(r'(?i)^y$')
        n_regex = re.compile(r'(?i)^n$')
        if wr_edit_regex.match(choice):
            edit_work_routine(id)
            return
        elif wr_add_exercise_regex.match(choice):
            wr_add_exercise(id)
            continue
            list_exercises_w_menu()
            continue
        elif wr_cut_exercise_regex.match(choice):
            selection_regex = re.compile(r'^\d{1,3}$')
            selection = input(f'Which exercise do you wish to delete? ')
            if selection_regex.match(selection):
                selection = int(selection)
                exercise_confirm = Exercise.find_by_id(selection)
                exercise = Exercise.get_all()
                ex_ids = []
                for exercises in exercise:
                    ex_ids.append(exercises.id)
                if selection in ex_ids:
                    if exercise_confirm.w_routine_id == id:
                        confirmation = input(f'\u001b[43mAre you sure you want to delete exercise {selection}?\u001b[0m Y/N ')
                        if y_regex.match(confirmation):
                            wr_cut_exercise(selection, id)
                        elif n_regex.match(confirmation):
                            print("")
                            print("**************************")
                            print(f'You have opted not to delete {selection}.')
                            print("**************************")
                            print(routine)
                            for exercises in exercise:
                                if exercises.w_routine_id == id:
                                    print(f'    {exercises}')
                        else:
                            print(f'\u001b[41m{confirmation} is invalid. Please try again.\u001b[0m')
                    else:
                        print(f'\u001b[41m{selection} is not associated with this workout routine. Please try again.\u001b[0m')
                else:
                    print(f'\u001b[41m{selection} is not a valid exercise option. Please try again.\u001b[0m')
            else:
                print('\u001b[41mPlease enter a numerical value that matches the exercise ID you wish to remove.\u001b[0m')
            continue
        elif wr_delete_regex.match(choice):
            confirmation = input("\u001b[43mDeleting this routine will delete all associated exercises.\u001b[0m\nDo you wish to continue? Y/N ")
            if y_regex.match(confirmation):
                wr_delete_exercises(id)
                delete_workout_routine(id)
                return
            elif n_regex.match(confirmation):
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
        elif prv_menu_regex.match(choice):
            workout_routines = WorkoutRoutine.get_all()
            for workout_routine in workout_routines:
                print(f'ID: {workout_routine.id}, Title: {workout_routine.title}')
            return
        elif x_regex.match(choice):
            exit_program()
        else:
            print(f'\u001b[41m{choice} is not a valid option. Please try again.\u001b[0m')
            print("")
            print("**************************")
            print("")
    return


def wr_choice_options_menu():
    print("**************************")
    print("")
    print(" >>  Type E to edit this workout routine")
    print(" >>  Type A to add a new exercise to workout routine")
    # print(" >>  Type C to cut an exercise from workout routine")
    print(" >>  Type D to delete this workout routine")
    print("     OR        ")
    print(" >>  Type R to return to the previous menu")
    # print(" >>  Type M to go back to main menu")
    print(" >>  Type X to exit program")
    print("")
    print("**************************")

def wr_choice_options_menu_w_cut():
    print("**************************")
    print("")
    print(" >>  Type E to edit this workout routine")
    print(" >>  Type A to add a new exercise to workout routine")
    print(" >>  Type C to cut an exercise from workout routine")
    print(" >>  Type D to delete this workout routine")
    print("     OR        ")
    print(" >>  Type R to return to the previous menu")
    # print(" >>  Type M to go back to main menu")
    print(" >>  Type X to exit program")
    print("")
    print("**************************")

    
def edit_work_routine(id):
    if workout_routine := WorkoutRoutine.find_by_id(id):
        t_regex = re.compile(r'(?i)^t$')
        e_regex = re.compile(r'(?i)^e$')
        b_regex = re.compile(r'(?i)^b$')
        x_regex = re.compile(r'(?i)^x$')
        ex_id = []
        exos = Exercise.get_all()
        for exercises in exos:
            if exercises.w_routine_id == id:
                ex_id.append(exercises.id)
        # breakpoint()
        if ex_id:
            print("")
            print("\u001b[36;1mChoose from the options below.\u001b[0m")
            print("")
            decision = input("  >>  Type T to update title:\n  >>  Type E to update equipment:\n  >>  Type B to update both:\n  >>  Type X to edit an exercise:\n**************************\n  >> ")
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
                    print(f"\u001b[41m{exercise_id} is invalid. Please try again.\u001b[0m")
            elif x_regex.match(decision):
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
                        prim_decision = input("What would you like to update?\nType T for title:\nType D for description:\nType R for reps:\nType S for sets:\nType W for workout routine id:\nType A for all:\n  >> ")
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
                    print("\u001b[41mError updating workout routine:\u001b[0m")
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
    exercise = Exercise.get_all()
    for exercises in exercise:
        if exercises.w_routine_id == int(id):
            print(f'    {exercises}')
    wr_choice_options(id)

def wr_add_exercise(id):
    title = input(f'Enter new exercise title: ')
    description = input(f'Enter new exercise description: ')
    reps_regex = re.compile(r'^\d{1,3}$')
    reps = input(f'Enter target number of reps for new exercise: ')
    sets_regex = re.compile(r'^\d{1,3}$')
    sets = input(f'Enter target number of sets for new exercise: ')
    w_routine_id = id
    if reps_regex.match(reps):
        if sets_regex.match(sets):
            try:
                exercise = Exercise.create(title, description, int(reps), int(sets), w_routine_id)
                wo_r = WorkoutRoutine.find_by_id(id)
                print("")
                print(f'\u001b[32;1mSuccess! {exercise.title} has been added to {wo_r.title}!\u001b[0m')
                print("")
            except Exception as exc:
                print("")
                print("\u001b[41mError creating exercise:\u001b[0m ", exc)
                print("")
        else:
            print("")
            print("\u001b[41mPlease enter numerical values for sets.\u001b[0m")
            print("")
    else:
        print("")
        print("\u001b[41mPlease enter numerical values for reps.\u001b[0m")
        print("")
    
    wo_r = WorkoutRoutine.find_by_id(id)
    print(wo_r)
    exercise = Exercise.get_all()
    for exercises in exercise:
        if exercises.w_routine_id == int(id):
            print(f'    {exercises}')
    
    
def wr_cut_exercise(selection, id):
    exercise = Exercise.find_by_id(selection)
    print("")
    print(f"\u001b[32;1mExercise {selection} has successfully been deleted.\u001b[0m")
    exercise.delete()
    print("")
    wo_r = WorkoutRoutine.find_by_id(id)
    print(wo_r)
    wr_list_exercises(id)


def delete_workout_routine(id):
    if workout_routine := WorkoutRoutine.find_by_id(id):
        workout_routine.delete()
        print("")
        print(f'\u001b[32;1mWorkout Routine {id} has been deleted.\u001b[0m')
        print("")

    workout_routines = WorkoutRoutine.get_all()
    for workout_routine in workout_routines:
        print(f'ID: {workout_routine.id}, Title: {workout_routine.title}')
    return
   
    
def wr_delete_exercises(id):
    exercises = Exercise.get_all()
    for exercise in exercises:
        if exercise.w_routine_id == id:
            exercise.delete()
    

def create_workout_routine():
    title = input(f'Enter the name of the new workout routine: ')
    equipment = input(f'Enter the equipment of the new routine: ')
    try:
        workout_routine = WorkoutRoutine.create(title, equipment)
        print("")
        print(f'\u001b[32;1mSuccess! {workout_routine.title} has been created!\u001b[0m')
        print("")
        wo = WorkoutRoutine.get_all()
        last_id = wo[-1].id
        wr_last = WorkoutRoutine.find_by_id(last_id)
        print(wr_last)
        wr_choice_options(last_id)
        return
    except Exception as exc:
        print("\u001b[41mError creating workout routine:\u001b[0m ", exc)
    return


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
    

# def menu():
#     choice = input("> ")
