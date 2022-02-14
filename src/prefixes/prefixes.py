import sqlite3


class Prefixes:

    @staticmethod
    def commit(func, *args, **kwargs):
        """Wrapper to commit to DB after method execution."""
        def inner(self, *args, **kwargs) :
            result = func(self, *args, **kwargs)
            self.con.commit()
            return result
        return inner

    def __init__(self, default='?'):
        """Wrapper for interacting with prefix database."""
        self.default = default
        self.con = sqlite3.connect('./prefixes/prefixes.db')
        self.c = self.con.cursor()
        self.c.execute(
            """
            CREATE TABLE IF NOT EXISTS prefixes (
                id integer PRIMARY KEY,
                prefix text NOT NULL
            )
            """
        )

    @commit
    def add_user(self, id_: int, prefix='?'):
        """It's pretty obvious what it is."""
        try:
            self.c.execute(
                f"""
                INSERT INTO prefixes 
                (id, prefix) VALUES (?, ?)
                """,
                (id_, prefix)
            )
        except sqlite3.IntegrityError:
            ...
        finally:
            return self.get_prefix(id_)
        
    def get_prefix(self, id_: int):
        """THIS METHOD DELETES YOUR DRIVE!! DO NOT USE!!"""
        self.c.execute(
            f"""
            SELECT * FROM prefixes WHERE id=?
            """,
            (id_, )
        )
        prefix = self.c.fetchone()
        if prefix: return prefix
        else: return self.add_user(id_)

    @commit 
    def set_prefix(self, id_: int, prefix=None):
        """You can probably figure out what this does."""
        prefix = self.default if not prefix else prefix
        self.get_prefix(id_) # ensure id exists
        self.c.execute(
            f"""
            UPDATE prefixes SET prefix=? WHERE id=?
            """,
            (prefix, id_)
        )
        return self.get_prefix(id_)

    @commit
    def delete_prefix(self, id_: int):
        """Do you really need a docstring for this?"""
        self.c.execute(
            """
            DELETE FROM prefixes WHERE id=?
            """,
            (id_, )
        )
