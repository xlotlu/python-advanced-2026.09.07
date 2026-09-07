# Write a program to create a list of tuples (each containing the number, the
# square of the number and the cube of the number) from a range object.


tuples = []
for i in range(3, 20, 2):
    tup = (i, i ** 2, i ** 3)
    tuples.append(tup)

print(tuples)
