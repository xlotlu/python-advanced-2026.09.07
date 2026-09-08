# bună dimineața


from functools import cache
from random import randint

@cache
def myrand(a, b):
    return randint(a, b)

# este echivalent cu,
# este "syntactic sugar" pentru:

def myrand(a, b):
    return randint(a, b)

myrand = cache(myrand)


# decoratorul este o funcție (un callable)
# care primește ca argument o funcție (un callable)
# și returnează o funcție (un callable)

# iată cum scriem o funcție ce returnează o funcție
# (specific una definită intern)

def func():
    
    def innerfunc():
        print("eu sunt interna")
        
    return innerfunc
func()
infunc = func()
infunc()

# acesta chiar este un decorator, inutil:
def mydeco(func):
    
    def _inner():
        print("eu sunt interna")
        
    return _inner

# care nu cunoaște semnătura funcției ce o decorează
# exemplu:
@mydeco
def myrand(a, b):
    return randint(a, b)
# ne obligă să rulăm ca:
myrand() # fără argumente

# un decorator care chiar face ceva,
# și respectă semnătura funcției:
def mydeco(func):
    
    def _inner(a, b):
        print("-- eu sunt interna")
        retval = func(a, b)
        print("-- tot interna, gata")
        return retval
        
    return _inner

@mydeco
def myrand(a, b):
    return randint(a, b)

myrand(1, 10)


# cum scriem un decorator care este agnostic de
# semnătura funcției pe care o decorează?
#
# traducere: vrem să pasăm toate argumentele și kwargs-urile:

def mydeco(func):
    def _inner(*args, **kwargs):
        print("-- eu sunt interna")
        retval = func(*args, **kwargs)
        print("-- tot interna, gata")
        return retval

    return _inner

# Exercițiu:
# știind acestea, scrieți un decorator
def timeit(func):
    pass
# ce printează timpul de execuție
# al funcției decorate


from datetime import datetime
# sau
# from time import time as now

def timeit(func):
    def _inner(*args, **kwargs):
        start = datetime.now()
        retval = func(*args, **kwargs)
        end = datetime.now()

        delta = (end - start).total_seconds()
        print(f"{func.__name__} executed in: {delta:.06f} seconds")
        return retval

    return _inner


# Exercițiul următor:
# un decorator care loghează
# numele funcției executate, cu toate argumentele sale
# cu return value, și durata de execuție

import sys
from functools import chain

def logit(func):
    LOG = "{func}({params}) -> {retval!r} :: {delta:.06f}s"

    def _inner(*args, **kwargs):
        start = datetime.now()
        retval = func(*args, **kwargs)
        end = datetime.now()

        delta = (end - start).total_seconds()

        _args = [repr(elem) for elem in args]
        _kwargs = [f'{k}={v!r}' for k, v in kwargs.items()]

        params = _args + _kwargs

        # sau, nu mai creăm liste intermediare:
        params = chain(
            (repr(elem) for elem in args),
            (f'{k}={v!r}' for k, v in kwargs.items())
        )

        print(
            LOG.format(
                func=func.__name__,
                params=", ".join(params),
                retval=retval,
                delta=delta,
            ),
            file=sys.stderr
        )

        return retval

    return _inner



# Dar!!! o funcție decorator care primește parametri?

# demo incomplet:
def logit(file=sys.stderr):
    print("» 1. sunt wrapperul din jurul decoratorului real")
    print("»    eu am primit argumentele pentru funcția decorator.")

    def _deco(func):
        print("» 2. eu sunt decoratorul real.")
        print("»    o decorez pe", func.__name__)

        def _inner(*args, **kwargs):
            print("» 3. eu sunt funcția decorată.")
            print("     mă execut.")
            print("     teoretic o să fac ceva cu argumentul `file`", repr(file))

            retval = func(*args, **kwargs)
            return retval

        return _inner

    return _deco



# Întrebare:
# pot pune atribute pe o funcție?
#
# Răspuns: da
# Exemplu util: memoizare pe un atribut
#               al funcției

def myfunc(x, y):
    k = (x, y)
    try:
        retval = myfunc._myfunc_cache[k]
    except KeyError:
        print("!cache miss")
        myfunc._myfunc_cache[k] = retval = x * y
    
    return retval
myfunc._myfunc_cache = {}


### Class-based decorator ###
#
# ocazie cu care învățăm că obiectele în Python
# (adică instanțele!) pot fi "executate", ca o funcție:

class MyClass:
    def __init__(self, x, y="default"):
        self.x = x
        self.y = y
        
    def __call__(self):
        print("eu sunt un obiect în plină execuție")
        return self.y * self.x

# Exercițiu:
# Scrieți o clasă `logit` ce funcționează ca decorator

# decoratorul este o funcție
# care primește ca argument o funcție
# și returnează o funcție

# tradus:

# decoratorul este un callable (spre exemplu o clasă)
# care primește ca argument un callable
# și returnează un obiect callable.

# dacă scriem un decorator-clasă,
# înseamnă că (pentru ca instanțele sale să fie callable),
# trebuie să îi implementăm metoda `__call__`.

# acesta este un decorator class-based minim, funcțional:
class logit:
    def __init__(self, func):
        print("» inițializat obiectul")
        self.func = func

    def __call__(self, *args, **kwargs):
        print("» execut funcția decorată")
        result = self.func(*args, **kwargs)
        return result

class logit:
    LOG_TEMPLATE = "{func}({params}) -> {retval!r} :: {delta:.06f}s"

    def __init__(self, func):
        self.func = func

    def __call__(self, *args, **kwargs):
        start = datetime.now()
        retval = self.func(*args, **kwargs)
        end = datetime.now()

        delta = (end - start).total_seconds()

        _args = [repr(elem) for elem in args]
        _kwargs = [f'{k}={v!r}' for k, v in kwargs.items()]

        params = _args + _kwargs

        print(
            self.LOG_TEMPLATE.format(
                func=self.func.__name__,
                params=", ".join(params),
                retval=retval,
                delta=delta,
            ),
            file=sys.stderr
        )

        return retval


# Exercițiu:
# transformați class-based decorator-ul de mai sus
# astfel încât să primească argumentul opțional
# file=sys.stderr

import _io

class logit:
    LOG_TEMPLATE = "{func}({params}) -> {retval!r} :: {delta:.06f}s"

    def __init__(self, file=sys.stderr):
        # cum împăcăm struțo-cămila?
        # anume, file poate să fie un writable stream
        # sau un string (sau altceva), care este
        # calea către fișier

        # verificare în funcție de ce tip are:
        if isinstance(file, _io.TextIOWrapper):
            self.file = file
        else:
            self.file = open(file, 'a', encoding="utf-8")

    def __call__(self, func):
        def inner(*args, **kwargs):
            start = datetime.now()
            retval = func(*args, **kwargs)
            end = datetime.now()

            delta = (end - start).total_seconds()

            _args = [repr(elem) for elem in args]
            _kwargs = [f'{k}={v!r}' for k, v in kwargs.items()]

            params = _args + _kwargs

            print(
                self.LOG_TEMPLATE.format(
                    func=func.__name__,
                    params=", ".join(params),
                    retval=retval,
                    delta=delta,
                ),
                file=self.file,
                flush=True,
            )

            return retval
        return inner

# situație:
@logit("/tmp/log.txt")
def myfunc(x, y):
    pass

@logit("/tmp/log.txt")
def myotherfunc():
    pass
# va deschide două file handlere către același fișier

# întrebare:
# cum ne-am asigura să existe o singură instanță
# de file handler pentru un nume de fișer dat?

# Singleton!
# este un "design pattern"
# dat fiind o clasă

class MyThing():
    pass

# dacă implementăm singleton, reiese că:

a = MyThing()
b = MyThing()

a is b
# adică există o singură instanță, întotdeauna

class MyDBConnection:
    pass

conn = MyDBConnection()

# "Multiton"!

# dat fiind o clasă

class MyThing():
    def __init__(self, param):
        pass

a = MyThing("param X")
b = MyThing("param X")
c = MyThing("param Y")
d = MyThing("param Y")
# atunci....
a is b
c is d
a is not c

# aplicat la...
class MyDBConnection:
    def __init__(self, dsn):
        pass

conn1 = MyDBConnection("oracle:something")
conn2 = MyDBConnection("oracle:something")
conn3 = MyDBConnection("postgres:something")



# Rămâne o întrebare:
# un decorator care funcționează și așa:
@logit
def myfunc():
    pass
# și așa:
@logit("/tmp/log.txt")
def myfunc():
    pass

