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

    @classmethod
    def create_table(cls):
        """ Create a new table to pass attributes of WorkoutRoutine instances"""
        sql = """
            CREATE TABLE IF NOT EXISTS workout_routines (
                id INTEGER PRIMARY KEY,
                name TEXT,
                location TEXT)
        """
        CURSOR.execute(sql)
        CONN.commit()

    @classmethod
    def drop_table(cls)
        """ Remove table if workout_routines table alreadye exists"""
        sql = """
            DROP TABLE IF EXISTS workout_routines;
        """
        CURSOR.execute(sql)
        CONN.commit()

    