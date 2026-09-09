# interceptare de setare de atribut:

class MyThing:
    def __init__(self, value):
        self.value = value

    def __setattr__(self, name, v):
        print(f"» setting {name} to {v!r}")
        if name == "bla":
            raise ValueError("nu-mi place de tine!")
        super().__setattr__(name, v)


# __setattr__ este entry-point unic pentru setare,
#
# pe când există două entry-point-uri posibile
# pentru getattr()

# 1: __getattr__ pentru atribute care nu există

class MyThing:
    def __init__(self, value):
        self.value = value

    def __setattr__(self, name, v):
        print(f"» setting {name} to {v!r}")
        if name == "bla":
            raise ValueError("nu-mi place de tine!")
        super().__setattr__(name, v)

    def __getattr__(self, name):
        print("» getattr pentru", name)
        print("  pentru că", name, "nu există!")
        if name == "bla":
            return 52
        else:
            raise AttributeError()

# 2: __getattribute__ pentru !!tot!! accesul

class MyThing:
    def __init__(self, value):
        self.value = value

    def __setattr__(self, name, v):
        if name == "bla":
            raise ValueError("nu-mi place de tine!")
        super().__setattr__(name, v)

    def __getattr__(self, name):
        print("» getattr pentru", name)
        print("  pentru că", name, "nu există!")
        if name == "bla":
            return 52
        else:
            raise AttributeError()

    def __getattribute__(self, name):
        print("!! în __getattribute__ pentru", name)
        # folosim asta cu grijă,
        # pentru că am interceptat flow-ul fundamental
        # de acces la atribute

        return super().__getattribute__(self, name)

    def method(self):
        print("în metodă")


# exemplu de singleton, cea mai simplă variantă:
# folosim __new__

class CollectionSingleton:
    _single_object = None

    # atenție. __new__ este un staticmethod!
    # (automat, conform specificației)
    def __new__(cls, *args, **kwargs):
        if not cls._single_object:
            cls._single_object = super().__new__(cls)

        return cls._single_object

    def __init__(self):
        print("mă inițializez")


# item access (acces "după index", "după cheie")
# a.k.a. subscriptable object

class CanItemAssign:
    def __init__(self):
        self.__collection = {}

    def __setitem__(self, key, value):
        self.__collection[key] = value

    def __getitem__(self, key):
        return self.__collection[key]


###########
# finally #
###########

# fluxul COMPLET de instanțiere al unui obiect:

class MyMeta(type):
    def __new__(mcls, name, bases, namespace):
        print("» inside the metaclass :: new:", name)
        print("                       :: namespace keys: ", *namespace.keys())
        # pasăm toate argumentele
        # pentru că inherit-uim pe type
        return super().__new__(mcls, name, bases, namespace)
        # și a returnat un new type, cu name="MyClass"

    def __init__(cls, name, bases, namespace):
        print("» inside the metaclass :: init")
        print("                       ::", cls)
        cls.MY_ATTR = 42
        cls.MY_OTHER_ATTR = "the meaning of life"

    def __call__(cls, *args, **kwargs):
        print("» inside the metaclass :: call")
        print("                       :: args:", args)
        print("                       :: kwargs:", kwargs)

        # putem returna un alt data-type de aici
        #import datetime
        #return datetime.date.today()

        instance = super().__call__(*args, **kwargs)
        # ^^ implementarea default execută
        #    __new__ și __init__ al clasei

        print("» inside the metaclass :: done call-ing")

        return instance


class MyClass(metaclass=MyMeta):
    MY_ATTR = 12

    def __new__(cls, *arg, **kwargs):
        print("! inside the class :: new")

        # ... și putem returna un alt data-type de aici
        #return "something"

        return super().__new__(cls) # nu pasăm args și kwargs
                                    # pentru că inherit-uim pe object

    def __init__(self, arg1, something="else"):
        print("! inside the class :: init")

    def regular_method(self):
        pass


obj = MyClass("un arg")
