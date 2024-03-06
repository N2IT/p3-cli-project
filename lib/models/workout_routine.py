from models.__init__ import CURSOR, CONN

class WorkoutRoutine:

    all = {}
    
    def __init__(self, title, equipment, id = None):
        self.id = id
        self.title = title
        self.equipment = equipment

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, title):
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
        pass
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
                title TEXT,
                equipment TEXT)
        """
        CURSOR.execute(sql)
        CONN.commit()

    @classmethod
    def drop_table(cls):
        """ Remove table if workout_routines table alreadye exists"""
        sql = """
            DROP TABLE IF EXISTS workout_routines;
        """
        CURSOR.execute(sql)
        CONN.commit()

    def save(self):
        """Insert a new row with the title and equipment values of the current WorkoutRoutine instance.  Update object id attribute using the primary key value of the new row."""
        sql = """
            INSERT into workout_routines (title, equipment)
            VALUES (?, ?)
        """
        CURSOR.execute(sql, (self.title, self.equipment))
        CONN.commit()

        self.id = CURSOR.lastrowid
        type(self).all[self.id] = self

    @classmethod
    def create(cls, title, equipment):
        """Check the new WorkoutRoutine does not already exist. Then initialize a new WorkoutRoutine instance and save the object to the database."""
        workout_routine = cls(title, equipment)
        workout_routine.save()
        return workout_routine

    def update(self):
        """Update table row related to the current WorkoutRoutine instance."""
        sql = """
            UPDATE workout_routines
            SET title = ?, equipment = ?
            WHERE id = ?
        """
        CURSOR.execute(sql, (self.title, self.equipment, self.id))
        CONN.commit()

    def delete(self):
        """Delete table row of current WorkoutRoutine instance."""
        sql = """
            DELETE FROM workout_routines
            WHERE id = ?
        """
        CURSOR.execute(sql, (self.id,))
        CONN.commit()

        del type(self).all[self.id]
        self.id = None

    @classmethod 
    def instance_from_db(cls, row):
        """Return a WorkoutRoutine object having the attribute values from the table row."""
        workout_routine = cls.all.get(row[0])
        if workout_routine:
            workout_routine.title = row[1]
            workout_routine.equipment = row[2]
        else:
            workout_routine = cls(row[1], row[2])
            workout_routine.id = row[0]
            cls.all[workout_routine.id] = workout_routine
        return workout_routine

    @classmethod
    def get_all(cls):
        """Return a list containing a WorkoutRoutine object per row in the table"""
        sql = """
            SELECT *
            FROM workout_routines
        """
        rows = CURSOR.execute(sql).fetchall()

        return [cls.instance_from_db(row) for row in rows]

    @classmethod
    def find_by_id(cls, id):
        """Return WorkoutRoutine object corresponding to the table row mathcing the specific id number"""
        sql = """
            SELECT *
            FROM workout_routines
            WHERE id = ?
        """
        row = CURSOR.execute(sql,(id,)).fetchone()
        return cls.instance_from_db(row) if row else None

    @classmethod
    def find_by_title(cls, title):
        """Return WorkoutRoutine object corresponding to the table row matching a speicific name"""
        sql = """
            SELECT *
            FROM workout_routines
            WHERE title = ?
        """

        row = CURSOR.execute(sql,(title,)).fetchone()
        return cls.instance_from_db(row) if row else None

    
    