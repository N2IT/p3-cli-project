class Workout:
    def __init__(self, exercise, date, sets, reps, weight):
        self.exercise = exercise
        self.date = date
        self.sets = sets
        self.reps = reps
        self.weight = weight

    def __repr__(self):
        return f'{self.exercise}\n{self.date}\n{self.sets}\n{self.reps}\n{self.weight}'