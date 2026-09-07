# Write a function that takes two numbers as arguments and returns their sum,
# difference, product, and quotient. Call the function and assign the result to
# 4 different variables.
def operations(x, y):
    return x + y, x - y, x * y, x // y


total, diff, prod, quot = operations(10, 2)
print(total, diff, prod, quot)

# Using * unpacking and range, print the numbers 1 to 20, separated by commas.
# You will have to provide an argument for print function's sep parameter for
# this exercise.
print(*range(1, 21), sep=", ")

# Modify your code from the previous exercise so that each number prints on a
# different line. You can only use a single print call.
print(*range(1, 21), sep="\n")

# Print a sentence using the following dictionary, the str.format method and
# ** unpacking:
country = {
    "name": "Romania",
    "population": "19 million",
    "capital": "Bucharest",
    "currency": "RON"
}
# E.g.
# Romania has a population of 19 million people. The capital is Bucharest
# and uses RON as currency.

print("{name} has a population of {population} million people. The capital is "
      "{capital} and uses {currency} as currency.".format(**country))
