from models.__init__ import CURSOR, CONN
from models.workout_routine import WorkoutRoutine

class Exercise:

    all = {}

    def __init__(self, title, description, reps, sets, w_routine_id, id = None):
        self.id = id
        self.title = title
        self.description = description
        self.reps = reps
        self.sets = sets
        self.w_routine_id = w_routine_id

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, title):
        if len(title) > 25:
            raise AttributeError("Title not to exceed 25 characters in length.")
        else:
            self._title = title

    @property
    def description(self):
        return self._description

    @description.setter
    def description(self, description):
        if len(description) < 10:
            raise AttributeError("Description should exceed 10 characters in length.")
        else:
            self._description = description

    @property
    def reps(self):
        return self._reps

    @reps.setter
    def reps(self, reps):
        if not isinstance(reps, int):
            raise AttributeError("Reps should be of type Integer.")
        else:
            self._reps = reps

    @property
    def sets(self):
        return self._sets

    @sets.setter
    def sets(self, sets):
        if not isinstance(sets, int):
            raise AttributeError("Sets should be of type Integer.")
        else:
            self._sets = sets

    @property
    def w_routine_id(self):
        return self._w_routine_id

    @w_routine_id.setter
    def w_routine_id(self, w_routine_id):
        if not isinstance(w_routine_id, int):
            raise AttributeError("The workout routine id should be of type integer")
        else:
            self._w_routine_id = w_routine_id

    def __repr__(self):
        return (
            f"<Exercise {self.id}: {self.title}, {self.description}, Target Reps: {self.reps}, Target Sets: {self.sets}" +
            f"Workout Routine ID: {self.w_routine_id}>"
        )

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
            UPDATE exercise
            SET title = ?, description = ?, reps = ?, sets = ?, w_routine_id = ?
            WHERE id = ?
        """
        CURSOR.execute(sql, (self.title, self.description, self.reps, self.sets, self.w_routine_id))
        CONN.commit()

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
            FROM exercise
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