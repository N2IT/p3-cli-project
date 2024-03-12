#!/usr/bin/env python3
# lib/debug.py
from models.exercise import Exercise
from models.workout_routine import WorkoutRoutine
from models.__init__ import CONN, CURSOR
import ipdb

WorkoutRoutine.drop_table()
WorkoutRoutine.create_table()
Exercise.drop_table()
Exercise.create_table()

wr1 = WorkoutRoutine.create('Monday Mashup', 'Dumbells')
wr2 = WorkoutRoutine.create('Tuesday Tri-sets', 'Body weight')
wr3 = WorkoutRoutine.create('HIIT Workout', 'None')
wr4 = WorkoutRoutine.create('Yoga', 'None')
wr4 = WorkoutRoutine.create('Heavy Weight', 'Bar, Weights, Dumbells')
wr5 = WorkoutRoutine.create('Bike Ride', 'Bicycle')

e1 = Exercise.create('Pushups', 'lie facing the floor and, keep back straight, raise body by pressing down on hands.', 10, 3, 2)
e2 = Exercise.create('Planks', 'n isometric core strength exercise', 1, 3, 2)
e3 = Exercise.create('Pull Ups', 'Use your body weight to bulk up your back and biceps', 10, 3, 2)
e4 = Exercise.create('Dips', 'Shred your chest and triceps with your body weight',10, 3, 2)
e5 = Exercise.create('Lunges', 'Like Squats but only 1 leg at at time',10, 3, 4)
e6 = Exercise.create('Squats', 'all the weight',10, 3, 4)
e7 = Exercise.create('Bench press', 'go big or go home', 15, 3, 4)


ipdb.set_trace()
