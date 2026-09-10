# Fundamentale:

In Python everything is a reference.
In Python everything is an object.

"Python is self-documenting."

# Utile:

String formatting: de citit

https://docs.python.org/3/library/string.html#format-examples

Date formatting (and parsing):

https://docs.python.org/3/library/datetime.html#format-codes


Design patterns:

https://refactoring.guru/design-patterns/


PEP-8 -- the styleguide:

https://peps.python.org/pep-0008/


# Protocolul de iterare:

```
for elem in obj:
    pass
```

face în spate:
 - transformă input-ul într-un iterator
 - rulează next() repetat pe obiectul rezultat
 - în caz că întâlnește StopIteration, înseamnă că
   for-ul s-a rulat cu succes.

tradus cu while:

```
obj = [1, 2, 3]
iobj = iter(obj)
while True:
    try:
        elem = next(iobj)
        print(elem)
    except StopIteration:
        break
```

# Pachete utile

$ pip install ipdb

și în cod:

```
import ipdb
ipdb.set_trace()
```

# Essential wisdom

There are 2 complex problems in programming:
- naming things
- cache invalidation
- off-by-one errors

```
>>> import this
```