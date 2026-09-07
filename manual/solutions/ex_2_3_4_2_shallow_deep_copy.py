# Create a list of lists matrix, where each inner list contains numbers. Create
# three other variables based on matrix:
# an alias
# a shallow copy
# a deep copy
# Try out different mutations (methods like append, remove, sort, item/slice
# assignment/deletion, etc) on matrix and see which of the copies change.
# Try out different mutations (methods like append, remove, sort, item/slice
# assignment/deletion, etc) on a inner list inside matrix and see which of the
# copies change.
import copy


matrix = [
    [1, 2, 3, 4],
    [10, 20, 30, 40],
    [0, 0, 0, 0],
]

alias = matrix
shallow = matrix[:]
deep = copy.deepcopy(matrix)

matrix.append([5, 6, 7, 7])
matrix.sort()
matrix[0] = []

print("original", matrix)
print("alias", alias)
print("shallow copy", shallow)
print("deep copy", deep)

matrix[1].append(10)
matrix[1].sort()
matrix[1][0] = 100

print("original", matrix)
print("alias", alias)
print("shallow copy", shallow)
print("deep copy", deep)
