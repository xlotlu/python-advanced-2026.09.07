class MyCollection:
    def __iter__(self): # dunder methods
        return MyIter()

class MyIter:
    def __next__(self):
        #raise StopIteration
        return "ceva"

# mai sus exemplu de implementare completă cu două clase,
# una ce suportă iter(), alta ce suportă next().

# mai jos, un hibrid ce se ocupă de tot:

class MyCollection:
    def __iter__(self):
        return self

    def __next__(self):
        #raise StopIteration
        return "ceva"


# Exercițiu:
# scrieți un class-based iterator
class FileLineStartsWith:
    def __init__(self, filename, substr):
        pass

# ce, când este iterat
# returnează liniile din `filename`
# care încep cu `substr`

for line in FileLineStartsWith("data/bash-README.txt", "The "):
    print(line)

# strategie:

# vom avea nevoie în interiorul __next__() de:
# - filepointer # deschidem fișierul în __init__ și punem atribut pe self.
# - substr      # punem atribut pe self în __init__

# ce facem în __next__()?
# începem să iterăm prin filepointer,
# verificăm condiția cu substr, dacă da: returnăm
# și cândva... când am terminat de iterat în filepointer,
# trebuie să facem raise StopIteration

class FileLineStartsWith:
    def __init__(self, filename, substr):
        self.file = open(filename)
        self.substr = substr

    def __iter__(self):
        return self

    def __next__(self):
        for line in self.file:
            if line.startswith(self.substr):
                return line.removesuffix("\n")

        self.file.close()
        raise StopIteration

# alternativ, "fără" să iterăm în __next__
class FileLineStartsWith:
    def __init__(self, filename, substr):
        self.filepointer = open(filename)
        self.substr = substr
        
    def __iter__(self):
        return self
    
    def __next__(self):
        return next(
            line.removesuffix("\n")
            for line in self.filepointer
            if line.startswith(self.substr)
        )

# Același exercițiu ca mai sus,
# dar pentru elementele dintr-o listă
class ListItemStartsWith:
    def __init__(self, lst, substr):
        pass

# testați cu:
lst = [
 "This is GNU Bash, version 5.3. Bash is the GNU Project's Bourne",
 'There are some user-visible incompatibilities between this version',
 'If you are a csh user and wish to convert your csh aliases to Bash',
 "The discussion list `bug-bash@gnu.org' often contains information",
 "The `help-bash@gnu.org' mailing list is used for questions about",
 "The `bashbug' program includes much of this automatically.",
 'If you would like to contact the Bash maintainers directly, send mail',
 'This distribution includes, in examples/bash-completion, a recent version',
 'The latest version of bash-completion is always available from',
 "If it's not a package from your vendor, you may install the included version.",
 'There are a number of example dynamically loadable builtin commands in the'
]

class ListItemStartsWith:
    def __init__(self, lst, substr):
        self.source = iter(lst)
        self.substr = substr
        
    def __iter__(self):
        return self
    
    def __next__(self):
        return next(
            item
            for item in self.source
            if item.startswith(self.substr)
        )



for line in ListItemStartsWith(lst, "The "):
    print(line)


# Puteți scrie un iterator general-purpose,
# ce să primească drept prim parametru orice obiect
# iterabil (fie un file pointer, fie o listă etc.)

class IterItemStartsWith:
    def __init__(self, source, substr):
        pass

# Răspuns: da, este exact același lucru ca mai sus.

class IterItemStartsWith:
    def __init__(self, source, substr):
        # ne asigurăm că lucrăm cu iterator intern,
        # astfel încât să avem streaming data,
        # conform cu input-ul, fără să o ia de la capăt
        self.source = iter(source)
        self.substr = substr
        
    def __iter__(self):
        return self
    
    def __next__(self):
        return next(
            item
            for item in self.source
            if item.startswith(self.substr)
        )


for l in IterItemStartsWith(lst, "The "):
    print(l)

with open("data/bash-README.txt") as fp:
    for l in IterItemStartsWith(fp, "The "):
        print(l)
