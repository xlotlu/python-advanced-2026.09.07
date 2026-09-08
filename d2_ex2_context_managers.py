# definiția completă a excepțiilor:

try:
    ceva = dict[k][idx]
except IndexError:
    pass
except KeyError:
    pass
except (TypeError, ValueError) as e:
    pass
except Exception as e:
    # acesta este catch-all. putem face ceva cu `e`.
    #
    # în general folosim acest pattern
    # pentru a captura excepția să o logăm
    # apoi o lăsăm să bubble up.
    raise e
else:
    # se rulează când nu a existat excepție
    pass
finally:
    # se rulează întotdeauna
    pass

# pe vremuri făceam:
def myfunc():
    fp = open("/tmp/my-file.txt", 'w')
    # cum ne asigurăm că se execută întotdeauna
    # fp.close()
    # în timp ce orice excepție trece mai departe?

    try:
        fp.write("ceva")
        # și alte operațiuni
        1 / 0
    finally:
        print("închid fișierul")
        fp.close()

# acum facem:

def myfunc():
    with open("/tmp/my-file.txt", 'w') as fp:
        fp.write("ceva")
        # și alte operațiuni
        1 / 0

class MyContext:
    def __init__(self, param):
        self.param = param
        print("» sunt un obiect inițializat", self)

    def __enter__(self):
        print("» sunt", self, "am intrat în ctx. manager")
        # dacă returnăm ceva aici
        # va fi capturat drept valoare variabilei
        # with ctxmanager as var: # <-- acest var
        return self

    def __exit__(self, exc_type, exc, tb):
        # argumentele sunt:
        # exception type, the exception, traceback.
        #
        # dacă nu există o excepție, vor fi
        # None, None, None.
        
        print("» am ieșit din ctx. manager")

# simplificat(?) folosind decoratorul contextmanager
# și sintaxa de generator function
from contextlib import contextmanager

@contextmanager
def MyContext():
    print("» am intrat în ctx. manager")
    yield
    print("» am ieșit din ctx. manager")

# Exercițiu:
# Scrieți timeit drept context manager,
# folosind o clasă

from time import perf_counter

class timeit:
    def __init__(self):
        pass

    def __enter__(self):
        self.start = perf_counter()
        # return self
        # ^^ suntem un context manager care nu necesită
        # acces la obiect

    def __exit__(self, exc_type, exc, tb):
        end = perf_counter()
        print("Duration", end - self.start)

# Exercițiu:
# Un `timeit` hibrid context manager / decorator,
# class-based

# încercăm să duplicăm cât mai puțin cod:
class timeit:
    def __init__(self, func=None):
        self.func = func

    def _start(self):
        self.start = perf_counter()

    def _end(self):
        return perf_counter() - self.start

    def __enter__(self):
        self._start()
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        delta = self._end()

        print(f'{delta:.06f}')

    def __call__(self, *args, **kwargs):
        self._start()
        result = self.func(*args, **kwargs)
        delta = self._end()

        print(f'{delta:.06f}')
        return result

# varianta "wow, cât de simplu era"
class timeit:
    def __init__(self, func=None):
        self.func = func

    def __enter__(self):
        self.start = perf_counter()
        return self

    def __exit__(self, exc_type, exc, tb):
        delta = perf_counter() - self.start
        print(f'{delta:.06f}')

    def __call__(self, *args, **kwargs):
        with self:
            return self.func(*args, **kwargs)

# TODO:
# să știți că există
# https://docs.python.org/3/library/contextlib.html
# contextlib.ContextDecorator și
# @contextmanager.contextlib
