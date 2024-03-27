#!/usr/bin/env python3
# lib/debug.py
from models.exercise import Exercise
from models.workout_routine import WorkoutRoutine
from models.user import User
from models.__init__ import CONN, CURSOR


WorkoutRoutine.drop_table()
WorkoutRoutine.create_table()
Exercise.drop_table()
Exercise.create_table()
User.drop_table()
User.create_table()

wr1 = WorkoutRoutine.create('Lower Body Strength', 'Dumbbells / Circuit Machines')
e1_wr1 = Exercise.create("Squats", "With or without weights", 10, 3, 1)
e2_wr1 = Exercise.create("Lunges", "With or without weights", 10, 3, 1)

wr2 = WorkoutRoutine.create('Cardio and Core', 'Optional: Bicycle')
wr3 = WorkoutRoutine.create('Cardio and Mobility', 'None')
wr4 = WorkoutRoutine.create('Upper Body Strength', 'Weight Bench / Dumbbells')
wr5 = WorkoutRoutine.create('Cardio and Full Body', 'None')
wr6 = WorkoutRoutine.create('Active Recovery and Flexibility', 'None')
wr7 = WorkoutRoutine.create('Endurance Cardio', 'Optional: Bicycle')

e1_wr2 = Exercise.create("Run, Hike, or Bicyle", "Any of those three options for 45 minutes minimum", 1, 1, 2)
e2_wr2 = Exercise.create("Plank", "Hold in push up position for 30 seconds", 0, 3, 2)

e1_wr3 = Exercise.create("Yoga","30 minutes incorporating hip, shoulder, spine and ankle mobility movements.", 1, 1, 3)
e2_wr3 = Exercise.create("Brisk Walk", "Walk for 30 minutes at an increased pace.", 1, 1, 3)

e1_wr4 = Exercise.create('Pushups', 'modify if necessary by keeping your knees on the floor. Keep abs engaged to support your back',12, 3, 4)
e2_wr4 = Exercise.create("Dumbbell Chest Press","Laying on back, push weights up in straight line from shoulders", 10, 3, 4)
e4_wr4 = Exercise.create("Tricep Dips", "Sit on elevated surface, extend legs, holding surface with hands, lower body til arms reach 90 degrees, lift back up.", 10, 3, 4)

e1_wr5 = Exercise.create("Jumping Jacks", "From standing position, jump with legs and arms spreading wide, then return to standing for 1 minute.", 0, 3, 5)
e3_wr5 = Exercise.create("Burpees", "From standing, dropt to squat then to plank position. Return to standing", 25, 3, 5)

e1_wr6 = Exercise.create("Walk or light bicycle", "Do either for 20 minutes at an easy pace", 1, 1, 6)
e2_wr6 = Exercise.create("Dynamic Stretching","Stretch muscles for both upper and lower body for 10 to 15 mins", 1, 1, 6)





