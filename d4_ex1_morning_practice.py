# morning practice is the best

# dat fiind metaclasa-exemplu
# d3_ex3_advanced_oop_concepts.MyMeta

# scrieți o clasă "multiton" astfel încât:

class MultitonMeta(type):
    pass

class DBConnection(metaclass=MultitonMeta):
    pass

# va rezulta în:
#a = DBConnection("dsn-1")
#b = DBConnection("dsn-1")
#c = DBConnection("dsn-2")

#a is b and a is not c

# există două puncte în fluxul de instanțiere
# de unde se returnează obiectul nou creat.
#
# acestea sunt:
# - metaclass.__call__
# - class.__new__
#
# faceți implementarea în metaclass.
#
# în concluzie: metaclass.__call__ va returna
# un obiect existent dacă există deja pentru
# acele argumente, altfel creează un obiect nou

# 1. versiunea cu cache-ul de instanțe per-clasă
#    (adică fiecare obiect-clasă are cache-ul său)

class MultitonMeta(type):
    def __init__(cls, name, bases, namespace):
        super().__init__(name, bases, namespace)
        cls._instances = {}

    def __call__(cls, *args, **kwargs):
        #key = (args, tuple(sorted(kwargs.items())))
        key = args + tuple(sorted(kwargs.items()))

        if key not in cls._instances:
            cls._instances[key] = super().__call__(*args, **kwargs)

        return cls._instances[key]

class Multiton(metaclass=MultitonMeta):
    pass

class DBConnection(Multiton):
    def __init__(self, dsn):
        self.dsn = dsn

# 2. versiunea cu cache-ul global
#    așezat pe metaclasă

class MultitonMeta(type):
    __instance_cache = {}

    def __call__(cls, *args, **kwargs):
        # atenție:
        # în cazul acesta clasa trebuie să fie parte din cheie
        key = (cls, ) + args + tuple(sorted(kwargs.items()))

        if key not in cls.__instance_cache:
            cls.__instance_cache[key] = super().__call__(*args, **kwargs)

        return cls.__instance_cache[key]

class Multiton(metaclass=MultitonMeta):
    pass

class DBConnection(Multiton):
    def __init__(self, dsn):
        self.dsn = dsn

class MyOther(Multiton):
    def __init__(self, *args, **kwargs):
        pass


class MyCls:
    __hidden_class_level_attr = "X"

    def mymethod(self):
        print(self.__hidden_class_level_attr)
        # will work
        # because it does its own whatever name-mangled access it needs


# Totul e un obiect!
# Un obiect este o instanță de ceva.
#        (adică al unei clase)
# Dar totul e un obiect!
# Deci clasa e un obiect!
# Deci clasa e o instanță a unei clase!
#
# Ea se numește metaclasă.

# Q: Cine creează obiectele noi?
# A: Metoda __new__
#
# Deci metoda __new__ a unei metaclase returnează clase
#
# clasele se pot crea doar de către `type()`
#
# deci metaclasa inherituiește type
