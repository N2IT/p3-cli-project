from models.__init__ import CURSOR, CONN
from models.workout_routine import WorkoutRoutine
import re


class Exercise:

    all = {}

    def __init__(self, title, description, reps, sets, w_routine_id, id = None):
        self.id = id
        self.title = title
        self.description = description
        self.reps = reps
        self.sets = sets
        self.w_routine_id = w_routine_id


    def __repr__(self):
        return (
            f"<Exercise {self.id}: Title: {self.title}, Description: {self.description}, Target Reps: {self.reps}, Target Sets: {self.sets}," + 
            f" Workout Routine ID: {self.w_routine_id}>"
        )

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, title):
        if not isinstance(title, str):
            raise Exception("Title must be a non-empty string")
            print("")
        else:
            if not 1 <= len(title) <= 25:
                raise Exception("Title must be between 1 and 25 characters.")
                print("")
            else:
                self._title = title

    @property
    def description(self):
        return self._description

    @description.setter
    def description(self, description):
        if not isinstance(description, str):
            raise Exception("Description must be of type string")
        else:
            if not 10 <= len(description) <= 120:
                raise Exception("Description should be between 10 and 120 characters in length")
            else:
                self._description = description

    @property
    def reps(self):
        return self._reps

    @reps.setter
    def reps(self, reps):
        from helpers import validate_integer_input
        try:
            valid_reps = validate_integer_input(reps)
            self._reps = valid_reps
        except ValueError:
            raise Exception("Invalid input for reps. Reps must be an integer.")

    @property
    def sets(self):
        return self._sets

    @sets.setter
    def sets(self, sets):
        from helpers import validate_integer_input
        try:
            valid_sets = validate_integer_input(sets)
            self._sets = valid_sets
        except ValueError:
            raise Exception("Invalid input for sets. Sets must be an integer.")

    @property
    def w_routine_id(self):
        return self._w_routine_id

    @w_routine_id.setter
    def w_routine_id(self, w_routine_id):
        from helpers import validate_integer_input
        if w_routine_id == 'Invalid routine number':
            raise ValueError("Invalid routine number")
        try:
            valid_w_routine_id = validate_integer_input(w_routine_id)
        except ValueError:
            raise Exception("Invalid input for routine number. Please try again.")
        if not WorkoutRoutine.find_by_id(valid_w_routine_id):
            raise ValueError("Invalid routine number")
        self._w_routine_id = valid_w_routine_id
        
            
    @classmethod
    def create_table(cls):
        """Creating a new table to persist the attributes of the Exercise instances """
        sql = """
            CREATE TABLE IF NOT EXISTS exercises (
                id INTEGER PRIMARY KEY,
                title TEXT,
                description TEXT,
                reps INTEGER,
                sets INTEGER,
                w_routine_id INTEGER,
                FOREIGN KEY (w_routine_id) REFERENCES workout_routines(id))
        """
        CURSOR.execute(sql)
        CONN.commit()

    @classmethod
    def drop_table(cls):
        """ Drop the table that persists exercise instances """
        sql = """
            DROP TABLE IF EXISTS exercises;
        """
        CURSOR.execute(sql)
        CONN.commit()
    
    def save(self):
        """Insert a new row with title, description, reps, sets, and id values of the current exercise instance. Update object id attribute using the primary key value of the new row. Ave the object in local dictionary using table row's PK as dict key."""
        sql = """
            INSERT INTO exercises (title, description, reps, sets, w_routine_id)
            VALUES (?, ?, ?, ?, ?)
        """
        CURSOR.execute(sql, (self.title, self.description, self.reps, self.sets, self.w_routine_id))
        CONN.commit()

        self.id = CURSOR.lastrowid
        type(self).all[self.id] = self

    def update(self):
        """Update the table row corresponding to the current Exercise instance."""
        sql = """
            UPDATE exercises
            SET title = ?, description = ?, reps = ?, sets = ?, w_routine_id = ?
            WHERE id = ?
        """
        CURSOR.execute(sql, (self.title, self.description, self.reps, self.sets, self.w_routine_id, self.id))
        CONN.commit()

    def delete(self):
        """Delete table row of current Exercises instance."""
        sql = """
            DELETE FROM exercises
            WHERE id = ?
        """
        CURSOR.execute(sql, (self.id,))
        CONN.commit()

        del type(self).all[self.id]
        self.id = None

    @classmethod
    def create(cls, title, description, reps, sets, w_routine_id):
        """ Initialize a new exercise object and save the object to the database. """
        exercise = cls(title, description, reps, sets, w_routine_id)
        exercise.save()
        return exercise

    @classmethod
    def instance_from_db(cls, row):
        """Return an Exercise objec having the attribute values from the table row."""

        exercise = cls.all.get(row[0])
        if exercise:
            exercise.title = row[1]
            exercise.description = row[2]
            exercise.reps = row[3]
            exercise.sets = row[4]
            exercise.w_routine_id = row[5]
        else:
            exercise = cls(row[1], row[2], row[3], row[4], row[5])
            exercise.id = row[0]
            cls.all[exercise.id] = exercise
        return exercise

    @classmethod
    def get_all(cls):
        """Return a list containing a Exercise object per row in the table"""
        sql = """
            SELECT *
            FROM exercises
        """

        rows = CURSOR.execute(sql).fetchall()

        return [cls.instance_from_db(row) for row in rows]

    @classmethod
    def find_by_id(cls, id):
        """Return a Exercise object corresponding to the table row matching the specified primary key"""
        sql = """
            SELECT *
            FROM exercises
            WHERE id = ?
        """

        row = CURSOR.execute(sql, (id,)).fetchone()
        return cls.instance_from_db(row) if row else None

    @classmethod
    def find_by_title(cls, title):
        """Return a Exercise object corresponding to first table row matching specified name"""
        sql = """
            SELECT *
            FROM exercises
            WHERE title is ?
        """

        row = CURSOR.execute(sql, (title,)).fetchone()
        return cls.instance_from_db(row) if row else None