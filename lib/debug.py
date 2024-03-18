#!/usr/bin/env python3
# lib/debug.py
from models.exercise import Exercise
from models.workout_routine import WorkoutRoutine
from models.user import User
from models.__init__ import CONN, CURSOR
import ipdb

WorkoutRoutine.drop_table()
WorkoutRoutine.create_table()
Exercise.drop_table()
Exercise.create_table()
User.drop_table()
User.create_table()

wr1 = WorkoutRoutine.create('Lower Body Strength', 'Dumbbells / Circuit Machines')
wr2 = WorkoutRoutine.create('Cardio and Core', 'Optional: Bicycle')
wr3 = WorkoutRoutine.create('Cardio and Mobility', 'None')
wr4 = WorkoutRoutine.create('Upper Body Strength', 'Weight Bench / Dumbbells')
wr5 = WorkoutRoutine.create('Cardio and Full Body', 'None')
wr6 = WorkoutRoutine.create('Active Recovery and Flexibility', 'None')
wr7 = WorkoutRoutine.create('Endurance Cardio', 'Optional: Bicycle')

e1_wr1 = Exercise.create("Squats", "With or without weights", 10, 3, 1)
e2_wr1 = Exercise.create("Lunges", "With or without weights", 10, 3, 1)
# e3_wr1 = Exercise.create("Hamstring Curls", "At home, substitute deadlifts, donkey kicks or hip presses with feet on the floor or a wall.", 12, 3, 1)
# e4_wr1 = Exercise.create("Calf Raises", "With or without weights", 15, 3, 1)

e1_wr2 = Exercise.create("Run, Hike, or Bicyle", "For 45 minutes minimum", 0, 0, 2)
e2_wr2 = Exercise.create("Plank", "Hold in push up position for 30 seconds", 0, 3, 2)
# e3_wr2 = Exercise.create("Forearm plank with twists", "Similar to plank but on forearms and twist to either side", 15, 3, 2)
# e4_wr2 = Exercise.create("Mountain Climbers", "Plank position, alternate knees to elbows for 1 minute", 0, 3, 2)

e1_wr3 = Exercise.create("Yoga","30 minutes incorporating hip, shoulder, spine and ankle mobility movements.", 0, 0, 3)
e2_wr3 = Exercise.create("Brisk Walk", "30 minutes", 0, 0, 3)

e1_wr4 = Exercise.create('Pushups', 'modify if necessary by keeping your knees on the floor. Keep abs engaged to support your back',12, 3, 2)
e2_wr4 = Exercise.create("Dumbbell Chest Press","Laying on back, push weights up in straight line from shoulders", 10, 3, 4)
# e3_wr4 = Exercise.create("Bent-over rows","Hinging your hips and leaning forward to lift barbell toward your body with a rowing movement pattern.", 10, 3, 4)
e4_wr4 = Exercise.create("Tricep Dips", "Sit on elevated surface, extend legs, holding surface with hands, lower body til arms reach 90 degrees, lift back up.", 10, 3, 4)

e1_wr5 = Exercise.create("Jumping Jacks", "From standing position, jump with legs and arms spreading wide, then return to standing for 1 minute.", 0, 3, 5)
# e2_wr5 = Exercise.create("High Knees", "Jog in place lifting your knees high towards your chest rapidly, maintaining a fast pace for 1 minute.", 0, 3, 5)
e3_wr5 = Exercise.create("Burpees, lunges, pushups", "burpees and jumping lunges for 30 secs ea, then 15 pushups", 0 , 3, 5)

e1_wr6 = Exercise.create("Walk or light bicycle", "Do either for 20 minutes at an easy pace", 0, 1, 6)
e2_wr6 = Exercise.create("Dynamic Stretching","Stretch muscles for both upper and lower body for 10 to 15 mins", 1, 1, 6)

# e1_wr7 = Exercise.create("Hike, bike, or brisk walk", "60 - 100 minutes of activity", 1, 1, 7)




#  = Exercise.create('Pushups', 'modify if necessary by keeping your knees on the floor. Keep abs engaged to support your back.', 10, 3, 2)
# e2_wr1 = Exercise.create('Dumbbell Chest Press')
# e2 = Exercise.create('Planks', 'n isometric core strength exercise', 1, 3, 2)
# e3 = Exercise.create('Pull Ups', 'Use your body weight to bulk up your back and biceps', 10, 3, 2)
# e4 = Exercise.create('Dips', 'Shred your chest and triceps with your body weight',10, 3, 2)
# e5 = Exercise.create('Lunges', 'Like Squats but only 1 leg at at time',10, 3, 4)
# e6 = Exercise.create('Squats', 'all the weight',10, 3, 4)
# e7 = Exercise.create('Bench press', 'go big or go home', 15, 3, 4)


# ipdb.set_trace()
