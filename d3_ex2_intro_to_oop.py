# Scrieți o clasă Point
# ce este insanțiată cu coordonatele x și y
# și:
# - instanțele sale au o reprezentare naturală
# - de asemenea, folosite în context de string
#   arată frumos: "(x, y)"
# - implementați o metodă translate(self, dx, dy)
#   ce schimbă coordonatele punctului
# - implementați o metodă get_distance_from_origin(self)

import math


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return f'{self.__class__.__name__}{self.as_tuple()}'

    def __str__(self):
        return f'({self.x}, {self.y})'

    @classmethod
    def from_tuple(cls, tup):
        return cls(*tup)

    @classmethod
    def from_dict(cls, dct):
        return cls(dct['x'], dct['y'])

    def translate(self, dx, dy):
        self.x += dx
        self.y += dy

    @property
    def distance_from_origin(self):
        return self.distance_between(
            self, self.__class__(0, 0)
        )

    @staticmethod
    def distance_between(p1, p2):
        return math.sqrt(
            (p2.x - p1.x) ** 2 + (p2.y - p1.y) ** 2
        )

    def as_tuple(self):
        return (self.x, self.y)

    def __eq__(self, other):
        return self.as_tuple() == other.as_tuple()

    def __lt__(self, other):
        return self.as_tuple() < other.as_tuple()

    # acum ar suporta +
    #def __add__(self, other):
    #    pass

    def __sub__(self, other):
        # TODO: return a vector here
        pass

class ThreeDPoint(Point):
    def __init__(self, x, y, z):
        # accesată din afară (via clasă),
        # metoda este o funcție. de aceea adăugăm self.
        #Point.__init__(self, x, y)

        # ^^ dar nu facem așa, pentru că ar trebui
        #    să avem grijă de inheritance manual.

        # vrem (aproape) întotdeauna să folosim:
        super().__init__(x, y)

        self.z = z

    def as_tuple(self):
        return (self.x, self.y, self.z)

    # not needed, the parent does all the work
    #def __repr__(self):
    #    return f'{self.__class__.__name__}({self.x}, {self.y}, {self.z})'

    @property
    def distance_from_origin(self):
        v = super().distance_from_origin
        # and then do something with v
        return v

    # not needed, the parent does all the work
    #def __eq__(self, other):
    #    return super().__eq__(other) and self.z == other.z
