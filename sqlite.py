import sqlite3 as sql
import os


class Database:

    def __init__(self):
        pass
        # super(Database, self).__init__()
        # self.conn = self.connect_to_db()
        # self.c = self.conn.cursor()
        # self.insert_into_db()

    def connect_to_db(self):
        if os.path.isfile("example.db"):
            try:
                conn = sql.connect('example.db')
                return conn
            except sql.Error as e:
                return None
        else:
            try:
                conn = sql.connect('example.db')
                self.init_db_setup(conn.cursor(), conn)
                return conn
            except sql.Error as e:
                return None

    def init_db_setup(self, c, conn):
        with conn:
            c.execute("""CREATE TABLE score (id INTEGER PRIMARY KEY, name text, time integer, size text)""")

    def fetch_all(self):
        conn = self.connect_to_db()
        if conn is not None:
            result = conn.cursor().execute("SELECT * FROM score").fetchall()
            conn.close()
            return result

    def fetch_by_size(self, size):
        conn = self.connect_to_db()
        if conn is not None:
            result = conn.cursor().execute("SELECT * FROM score WHERE size = ?", (size,)).fetchall()
            conn.close()
            return result

    def insert_value(self, name, time, size):
        conn = self.connect_to_db()
        if conn is not None:
            with conn:
                c = conn.cursor()
                c.execute("INSERT INTO score(name, time, size) VALUES (?, ?, ?)", (name, time, size))
            conn.close()

    def update_value(self, name, time, id):
        conn = self.connect_to_db()
        if conn is not None:
            with conn:
                conn.cursor().execute("UPDATE score SET name = ?, time = ? where id = ?", (name, time, id))
            conn.close()

    def handle_value(self, name, time, size):
        table = self.fetch_by_size(size)
        if len(table) == 0:
            self.insert_value(name, time, size)
            return

        conn = self.connect_to_db()
        if conn is not None:

            fix_score = False
            past_row = None

            for row in table:
                if time < row[2] and fix_score is False:
                    self.update_value(name, time, row[0])
                    past_row = row
                    fix_score = True
                elif fix_score is True:
                    self.update_value(past_row[1], past_row[2], row[0])
                    past_row = row

            if len(table) < 3 and past_row is None:
                self.insert_value(name, time, size)
            elif len(table) < 3 and past_row is not None:
                self.insert_value(past_row[1], past_row[2], size)
            conn.close()


# db = Database()
# db.handle_value("Roger", 182, "huge")
# print(db.fetch_by_size("huge"))
