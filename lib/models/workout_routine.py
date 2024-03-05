class WorkoutRoutine:
    def __init__(self, name):
        self.name = name
        self.exercises = []

    def add_exercise(self, workout):
        self.exercises.append(workout)

    def __repr__(self):
        return f'Workout Routine: {self.name}\nExercises: {self.exercises}'

    