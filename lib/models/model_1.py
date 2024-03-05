from __init__ import CURSOR, CONN

class Exercise:

    all = {}

    def __init__(self, title, description):
        self._title = title
        self._description = description
        self._workout_routine = None
        
        
    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, title):
        if 5 < len(title) < 15:
            self._title = title

    @property
    def description(self):
        return self._description

    @description.setter
    def description(self, description):
        if 10 < len(description) < 35:
            self._description = description
        else:
            raise TypeError("Description must be a certain character count")

    @property
    def workout_routine(self):
        return self._workout_routine

    @workout_routine.setter
    def workout_routine(self, value):
        if not isinstance(value, WorkoutRoutine):
            raise TypeError("WorkoutRoutine must be instance of WorkoutRoutine class.")
        self._workout_routine = value

    def get_all():
        return [exercise for exercise in Exercise.all]

    @classmethod
    def create_table(cls):
        """ Create a new table to persist the attributes of Exercise instances """
        sql = """
            CREATE TABLE IF NOT EXISTS exercises (
                id INTEGER PRIMARY KEY,
                title TEXT,
                description TEXT,
            )
        """
        CURSOR.execute(sql)
        CONN.commit()

    @classmethod
    def drop_table(cls):
        """ Drop the table that persists Exercise instances """
        sql = """
            DROP TABLE IF EXISITS exercsises;
        """
        CURSOR.execute(cls)
        CONN.commit()

    def __repr__(self):
        return f'Title: {self.title}\nDescription: {self.description}'
    
class WorkoutRoutine:
    
    def __init__(self, title):
        self.title = title

    def exercises(self):
        return [ exercise for exercise in Exercise.all if exercise.workout_routine == self]

    def add_exercise(self, exercise):
        if not isinstance(exercise, Exercise):
            raise TypeError("Exercise must be of Exercise class.")
        exercise.workout_routine = self

    def __repr__(self):
        return f'Title: {self.title}\n'



class WorkoutLog:
    pass




