# Create a context manager to measure the time taken by a block of code. Do it
# with both methods presented here (function and class based context managers).
import sqlite3
import time
from contextlib import contextmanager


@contextmanager
def measure_time():
    time_start = time.time()
    try:
        yield
    finally:
        time_diff = time.time() - time_start
        print(f"Execution took {time_diff:.4f}s")


class MeasureTime:
    def __init__(self, unit="s"):
        if unit not in ("s", "m"):
            raise ValueError("Unexpected time unit. Supported values (s, m).")
        self.unit = unit

    def __enter__(self):
        self.time_start = time.time()

    def __exit__(self, exc_type, exc_val, exc_tb):
        time_diff = time.time() - self.time_start
        if self.unit == "m":  # if unit is milliseconds
            time_diff *= 1000
        print(f"Execution took {time_diff:.4f}{self.unit}")


with measure_time():
    for i in range(2000):
        for j in range(2000):
            prod = i * j
            # if i == 1900:
            #     raise Exception


with MeasureTime("m"):
    for i in range(2000):
        for j in range(2000):
            prod = i * j


# The following code creates a database connection, creates a table and inserts
# some rows:
#
# import sqlite3
#
# con = sqlite3.connect("tutorial.db")
# cur = con.cursor()
# cur.execute("CREATE TABLE movie(title, year, score)")
# cur.execute("""
#     INSERT INTO movie VALUES
#         ('Monty Python and the Holy Grail', 1975, 8.2),
#         ('And Now for Something Completely Different', 1971, 7.5)
# """)
# con.commit()
# res = cur.execute("SELECT score FROM movie")
# print(res.fetchall())
#
# con.close()
# Create a context manager to handle a database connection. The context manager
# will return the connection object on setup and will close the connection on
# teardown.

@contextmanager
def manage_db_connection(db_name):
    connection = sqlite3.connect(db_name)
    try:
        yield connection
    finally:
        connection.close()


with manage_db_connection("example.db") as con:
    cur = con.cursor()
    try:
        cur.execute("CREATE TABLE movie(title, year, score)")
    except sqlite3.OperationalError as ex:
        print(ex)
    cur.execute("""
        INSERT INTO movie VALUES
            ('Monty Python and the Holy Grail', 1975, 8.2),
            ('And Now for Something Completely Different', 1971, 7.5)
    """)
    con.commit()
    res = cur.execute("SELECT score FROM movie")
    print(res.fetchall())

try:
    cur.execute("SELECT score FROM movie")
except sqlite3.ProgrammingError as ex:
    print(ex)
