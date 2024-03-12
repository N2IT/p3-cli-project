import os
import re
from models.workout_routine import WorkoutRoutine
from models.exercise import Exercise 

def list_exercises_w_menu():
    exercise = Exercise.get_all()
    for exercises in exercise:
        print(f'ID: {exercises.id}, Title: {exercises.title}')

