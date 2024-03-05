from exercise import Exercise
from workout_routine import WorkoutRoutine
from workout import Workout


wr1 = WorkoutRoutine('Monday Mashup')
wr2 = WorkoutRoutine('Tuesday Tri-sets')
wr3 = WorkoutRoutine('Wednesday meditation')

e1 = Exercise('Pushups', 'Great for core, shoulders, back, chest, and triceps')
e2 = Exercise('Planks', 'Core exercise to trim the waistline')
e3 = Exercise('Pull Ups', 'Use your body weight to bulk up your back and biceps')
e4 = Exercise('Dips', 'Shred your chest and triceps with your body weight')

wr1.add_exercise(e1)
wr1.add_exercise(e2)
wr1.add_exercise(e3)
wr1.add_exercise(e4)

wr1_e1 = Workout(wr1, "2024-3-5", 3, 20, None)

print(wr1_e1)