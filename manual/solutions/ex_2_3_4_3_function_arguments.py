# Considering the following function:
# def merge(first, second):
#     first += second
#     return first
# call it with parameters of the following types: int, str, tuple, list. Use a
# global variable as the first parameter and a value created on the spot as the
# second parameter. Print the result and the global variable. Is the global
# variable changed?

def merge(first, second):
    first += second
    return first


my_int = 562
my_str = "hello"
my_tuple = (6, 1, 3)
my_list = [4, 6, 1]

print("Modified", merge(my_int, 34))
print("Original", my_int)

print("Modified", merge(my_str, " world"))
print("Original", my_str)

print("Modified", merge(my_tuple, (3, 4)))
print("Original", my_tuple)

print("Modified", merge(my_list, [3, 4]))
print("Original", my_list)
