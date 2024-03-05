from workout_routine import WorkoutRoutine

class Exercise:
    def __init__(self, name, description):
        self.name = name
        self.description = description


    def __repr__(self):
        return f'Exercise Title: {self.name}\nDescription: {self.description}'