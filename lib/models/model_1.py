from __init__ import CURSOR, CONN

class Exercise:

    all = {}

    def __init__(self, title, description, id = None):
        self.id = id
        self._title = title
        self.description = description
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
        if 10 < len(description):
            self._description = description
        else:
            raise TypeError("Description must be more than 10 characters.")

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

    def __repr__(self):
        return f'Exercise {self.id}: {self.title}, {self.description}'
    
    @classmethod
    def create_table(cls):
        """ Create a new table to persist the attributes of Exercise instances """
        sql = """
            CREATE TABLE IF NOT EXISTS exercises (
            id INTEGER PRIMARY KEY,
            title TEXT,
            description TEXT
            )
        """
        CURSOR.execute(sql)
        CONN.commit()

    @classmethod
    def drop_table(cls):
        """ Drop the table that persists Exercise instances """
        sql = """
            DROP TABLE IF EXISTS exercises;
        """
        CURSOR.execute(sql)
        CONN.commit()

    def save(self):
        """ Insert a new row with the title and description of the current Exercise instance. Update object id attribute using the primary key value of new row.
        """
        sql = """
            INSERT INTO exercises (title, description)
            VALUES (?, ?)
        """

        CURSOR.execute(sql, (self.title, self.description))
        CONN.commit()

        self.id = CURSOR.lastrowid
        type(self).all[self.id] = self

    @classmethod
    def instance_from_db(cls, row):
        """Return an Exercise object having the attribute values from the table row."""

        exercise = cls.all.get(row[0])
        if exercise:
            exercise.title = row[1]
            exercise.description = row[2]
        else:
            exercise = cls(row[1], row[2])
            exercise.id = row[0]
            cls.all[exercise.id] = exercise
        return exercise


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
        return f'Title: {self.title}'



class WorkoutLog:
    pass




