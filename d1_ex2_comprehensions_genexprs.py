# Scrieți o funcție ce primind un iterabil
# cu numere, returnează o listă cu
# pătratele acestora

def squares(iter):
    # Pattern de acumulare
    # 1. instanțiem obiectul final
    out = []
    # 2. iterăm în sursă
    for v in iter:
        # 3. calculăm
        v = v ** 2
        # 4. acumulăm
        out.append(v)
    # 5. returnăm
    return out

# cu list comprehension:
def squares(iter):
    return [v ** 2 for v in iter]

# sintaxa completă:
# cerință: lista pătratelor numerelor impare

def odd_squares(iter):
    out = []
    for v in iter:
        if v % 2 == 1:
            v = v ** 2
            out.append(v)

    return out


def odd_squares(iter):
    return [
        v ** 2
        for v in iter
        if v % 2 == 1
    ]

# ^^ this was list comprehension.

# now: dictionary comprehension.

# creați un dicționar cu cheia nr-ul
# și valoarea pătratul său,
# pentru numerele de la 1 la 9

d = {}
for v in range(1, 10):
    d[v] = v ** 2

{
    v: v ** 2
    for v in range(1, 10)
}

# set comprehension:
# creați setul cu pătratele numerelor din
# lista
lst = [1, 2, 5, 3, 2, 1, 2, 4]

{
    v ** 2
    for v in lst
}


# "tuple comprehension" :: nu există

(
    v ** 2
    for v in lst
)

# în schimb creează un "generator expression",
# echivalent cu:

def squares(lst):
    for v in lst:
        yield v ** 2


# Task:
# aflați suma pătratelor numerelor impare de la 0 la 9 (inclusiv)
# folosind `sum`, `filter`, `range`, și fără a crea liste intermediare

sum(
    v ** 2
    for v in filter(
        lambda v: v % 2 == 1,
        range(1, 10)
    )
)
