import os
import re
from models.workout_routine import WorkoutRoutine
from models.exercise import Exercise

def refresh_exercises_list():
    global exercises
    exercises = Exercise.get_all()

def list_exercises_w_menu():
    ex_id = []
    print("")
    print("\u001b[36;1mHere are all exercises currently on record.\u001b[0m")
    print("")
    # breakpoint()
    while True:
        exercise = Exercise.get_all()
        for exercises in exercise:
            print(f'ID: {exercises.id}, Title: {exercises.title}')
            ex_id.append(str(exercises.id))
        ex_menu_options()
        breakpoint()
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
                print(f"\u001b[36;1mHere are the details for exercise {choice}:\u001b[0m")
                print("")
                print(ex)
            else: 
                print(f'\u001b[41mExercise {choice} not found\u001b[0m')
            ex_choice_options(choice)
        elif x_regex.match(choice):
            from wr_helpers import exit_program
            exit_program()
        else:
            print(f'\u001b[41m{choice} is not valid. Please choose again. IS THIS THE ERROR IM LOOKING FOR?\u001b[0m')
    return


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
        Exercise.get_all()
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
            confirmation = input("\u001b[43mDo you wish to delete this exercise?\u001b[0m Y/N ")
            if y_regex.match(confirmation):
                ex_delete_exercise(id)
                return
            elif n_regex.match(confirmation):
                print(f"You have opted not to delete exercise {id}.")
                print("")
                continue
            else:
                print(f'\u001b[41m{confirmation} is not a valid option. Please try again.\u001b[0m')
                print("")
                print("**************************")
                print("")
                ex_choice_options(id)
            return
        elif prv_menu_regex.match(choice):
            # Exercise.get_all()
            # exercise = Exercise.get_all()
            # for exercises in exercise:
            #     print(f'ID: {exercises.id}, Title: {exercises.title}')
            return
        elif x_regex.match(choice):
            from wr_helpers import exit_program
            exit_program()
        else:
            print(f'\u001b[41m{choice} is not a valid option. Please try again.\u001b[0m')
            print("")
            print("**************************")
            print("")
    return


def ex_choice_options_menu():
    print("**************************")
    print("")
    print(" >>  Type E to edit this exercise")
    print(" >>  Type D to Delete this exercise")
    print("     OR        ")
    print(" >>  Type R to return to the previous menu")
    print(" >>  Type X to exit program")
    print("")
    print("**************************")


def edit_exercise(id):
    if exercise := Exercise.find_by_id(id):
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
                print(exercise)
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
                print(exercise)
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
                print(exercise)
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
                print(exercise)
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
                        print(exercise)
                        # breakpoint()
                        print("")
                        print(f'\u001b[32;1mSuccess! {exercise.title.upper()} is now associated to your new workout routine, {new_wr.title.upper()}.\u001b[0m')
                        exercise.update()
                        return
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
                        print(exercise)
                        exercise.update()
                        return
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
                        return
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
        print(f'\u001b[41mWorkout Routine {id} not found.\u001b[0m')


def ex_delete_exercise(id):
    if exercise := Exercise.find_by_id(id):
        exercise.delete()
        print("")
        print(f'\u001b[32;1mExercise {id} has been deleted.\u001b[0m')
        print("")
    else:
        print(f'\u001b[41mWorkout Routine {id} not found.\u001b[0m')
    
    exercises = Exercise.get_all()
    for exercises in exercises:
        print(f'ID: {exercises.id}, Title: {exercises.title}')


# def create_exercise():
#     print("You have opted to create a new exercise.")
#     title = input('Enter a title for your exercise: ')
#     description = input('Enter a description of your exercise: ')
#     reps = input('Enter the target number of reps for your exercise: ')
#     sets = input('Enter the target number of sets for your exercise: ')
#     print("")
#     print('You will need to assign this exercise to a workout routine.')
#     new_regex = re.compile(r'(?i)^n$')
#     exist_regex = re.compile(r'(?i)^e$')
#     print("")
#     decision = input(f'Would you like to create a new Workout Routine for this exercise or assign to an existing?\n  >>  Type N for New | Type E for Exisiting: ')
#     print("")
#     if new_regex.match(decision):
#         print("You have opted to create a new workout routine.")
#         print("")
#         wr_title = input('Enter new workout routine title: ')
#         wr_equipment = input('Enter new workout routine equipment: ')
#         try:
#             new_wr = WorkoutRoutine.create(wr_title, wr_equipment)
#             wr = WorkoutRoutine.get_all()
#             w_routine_id = int(wr[-1].id)
#             new_exercise = Exercise.create(title, description, int(reps), int(sets), int(w_routine_id))
#             print("")
#             print(f'\u001b[32;1mSuccess! Your new exercise,{new_exercise.title}, is now associated with your new workout routine, {new_wr.title}.\u001b[0m')
#             print("")
#             Exercise.get_all()
#         except Exception as exc:
#             print("")
#             print("\u001b[41mError creating exercise:\u001b[0m ", exc)
#             print("")
#     elif exist_regex.match(decision):
#         wo = WorkoutRoutine.get_all()
#         print(f'\u001b[36;1mCurrent Workout Routines in database:\u001b[0m')
#         for wos in wo:
#             print(f'ID: {wos.id},Title: {wos.title}')
#         w_routine_id_regex = re.compile(r'^\d{1,3}$')
#         w_routine_id = input(f'Enter the workout routine id number you wish to add this exercise: ')
#         if w_routine_id_regex.match(w_routine_id):
#             try:
#                 exercise = Exercise.create(title, description, int(reps), int(sets), int(w_routine_id))
#                 print("")
#                 print(f'\u001b[32;1mSuccess! Your new exercise, {exercise.title.upper()} has been created and is associated to workout routine number {w_routine_id}.\u001b[0m')
#                 print("")
#                 Exercise.get_all()
#             except Exception as exc:
#                 print("")
#                 print("\u001b[41mError creating exercise:\u001b[0m ", exc)
#                 print("")
#         else: 
#             print("")
#             print("\u001b[41mPlease enter a valid workout routine id number.\u001b[0m")
#             print("")
#     else:
#         print(f'\u001b[41m{decision} is not a valid option. Please try again.\u001b[0m')
#         return
#     exos = Exercise.get_all()
#     latest_exer = exos[-1]
#     print(latest_exer)
#     ex_choice_options(latest_exer.id)
#     return Exercise.get_all()
    
def create_exercise():
    title = input('Enter a title for your exercise: ')
    description = input('Enter a description of your exercise: ')
    reps = input('Enter the target number of reps for your exercise: ')
    sets = input('Enter the target number of sets for your exercise: ')
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
    exos = Exercise.get_all()
    latest_exer = exos[-1]
    print(latest_exer)
    ex_choice_options(latest_exer.id)
    Exercise.get_all()
    