from models.__init__ import CURSOR, CONN

class WorkoutRoutine:
    
    def __init__(self, title, equipment, id = None):
        self.id = id
        self.title = title
        self.equipment = equipment

    @property
    def title(self):
        return self._title

    @title.setter(self, title):
        if len(title) > 20:
            raise TypeError("Title must not exceed 20 characters.")
        else:
            self._title = title
    
    @property
    def equipment(self):
        return self._equipment

    @equipment.setter
    def equipment(self, equipment):
        if len(equipment) > 25:
            raise TypeError("Equipment must not exceed 25 characters ")
        else:
            self._equipment = equipment

    def exercises(self):
        # update here to pull from exercises table

    def add_exercise(self, exercise):
        if not isinstance(exercise, Exercise):
            raise TypeError("Exercise must be of Exercise class.")
        exercise.workout_routine = self

    def __repr__(self):
        return f'<Workout Routine {self.id}: {self.title}, {self.equipment}'