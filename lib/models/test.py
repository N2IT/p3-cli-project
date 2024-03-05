from model_1 import (
    Exercise, WorkoutRoutine
)
Exercise.drop_table()
Exercise.create_table()

wr1 = WorkoutRoutine('Monday Mashup')
wr2 = WorkoutRoutine('Tuesday Tri-sets')
wr3 = WorkoutRoutine('Wednesday HIIT Workout')

e1 = Exercise.create('Pushups', 'lie facing the floor and, keep back straight, raise body by pressing down on hands.')
# e2 = Exercise('Pushupsallthewaytothegroundandbackagain', 'lie facing the floor and, keep back straight, raise body by pressing down on hands.')




# def Testing():
#     e1 = Exercise('Pushups', 'lie facing the floor and, keep back straight, raise body by pressing down on hands.')
#     e2 = Exercise('Pushups', 'lie facing the floor and, keep back straight, raise body by pressing down on hands.')
#     # e2 = Exercise('Planks', 'n isometric core strength exercise that involves maintaining a position similar to a push-up for the maximum possible time.')
#     # e2.save()
#     # e3 = Exercise('Pull Ups', 'Use your body weight to bulk up your back and biceps')
#     # e3.save()
#     # e4 = Exercise('Dips', 'Shred your chest and triceps with your body weight')
#     # e4.save()
#     # e5 = Exercise("one armed pushups", "lie facing the floor and, place one arm behind back, spread feet for support, keep back straight, raise body by pressing down on one hand.")
#     # e5.save()
#     # e6 = Exercise("one armed pushups", "lie facing the floor and, place one arm behind back, spread feet for support, keep back straight, raise body by pressing down on one hand.")
#     print("hear")

# Testing()

# wr1.add_exercise(e1)
# wr1.add_exercise(e2)
# wr1.add_exercise(e3)
# wr1.add_exercise(e4)

# wr2.add_exercise(e2)
# wr2.add_exercise(e4)

# wr3.add_exercise(e1)
# wr3.add_exercise(e3)





# wr1_e1 = Workout(wr1, "2024-3-5", 3, 20, None)

# print(Exercise.get_all())
# wr1.add_exercise(e1)
# wr2.add_exercise(e3)
# wr1.add_exercise(e2)
# wr1.add_exercise(e3)
# wr1.add_exercise(e4)

# print(Exercise.get_all()[0].workout_routine)
# print(wr1.exercises())


