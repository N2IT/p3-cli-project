from models.__init__ import CURSOR, CONN


class User:

    def __init__(self, name):
        self.name = name

    all = {}

    def __repr__(self):

        return f'<User ID: {self.id}: Name: {self.name}'

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        if len(name) > 0 and isinstance(name, str):
            self._name = name
        else:
            raise Exception("Title must be between 1 and 25 characters.")
            print("")
    
    @classmethod
    def create_table(cls):
        """Creating a new table to persist the attributes of the Exercise instances """
        sql = """
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY,
                name TEXT)
        """
        CURSOR.execute(sql)
        CONN.commit()

    @classmethod
    def drop_table(cls):
        """ Drop the table that persists exercise instances """
        sql = """
            DROP TABLE IF EXISTS users;
        """
        CURSOR.execute(sql)
        CONN.commit()
    
    def save(self):
        """Insert a new row with name of current user instance."""
        sql = """
            INSERT INTO users (name)
            VALUES (?)
        """
        CURSOR.execute(sql, (self.name,))
        CONN.commit()

        self.id = CURSOR.lastrowid
        type(self).all[self.id] = self
    
    @classmethod
    def create(cls, name):
        """ Initialize a new user object and save the object to the database. """
        user = cls(name)
        user.save()
        return user

    def delete(self):
        """Delete table row of current user instance."""
        sql = """
            DELETE FROM users
            WHERE id = ?
        """
        CURSOR.execute(sql, (self.id,))
        CONN.commit()

        del type(self).all[self.id]
        self.id = None

    @classmethod 
    def instance_from_db(cls, row):
        """Return a User object having the attribute values from the table row."""
        user = cls.all.get(row[0])
        if user:
            user.name = row[1]
        else:
            user = cls(row[1])
            user.id = row[0]
            cls.all[user.id] = user
        return user

    @classmethod
    def get_all(cls):
        """Return a list containing a User object per row in the table"""
        sql = """
            SELECT *
            FROM users
        """
        rows = CURSOR.execute(sql).fetchall()

        return [cls.instance_from_db(row) for row in rows]





