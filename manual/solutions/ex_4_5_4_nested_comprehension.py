# Write a nested set comprehension to generate a set of all unique pairs (i, j)
# where i is from the list [1, 2, 3] and j is from the list [1, 3, 5].
l1 = [1, 2, 3]
l2 = [1, 3, 5]
pairs = {(x, y) for x in l1 for y in l2}
print(pairs)


# Write a nested set comprehension to flatten a nested list [[1, 2, 3, 4],
# [4, 5, 6, 7], [6, 7, 8, 9]] -> {1, 2, 3, 4, 5, 6, 7, 8, 9}.

nested_list = [[1, 2, 3, 4], [4, 5, 6, 7], [6, 7, 8, 9]]
flat_set = {item for sublist in nested_list for item in sublist}

# Write a nested dictionary comprehension to create a dictionary where the keys
# are words and the values are dictionaries of occurrences (keys -> characters,
# values -> number of occurrences in word), starting from a sentence. E.g.
# text = "hello everyone"
# # should produce
# occurrences_dict = {
#     'hello': {'h': 1, 'e': 1, 'l': 2, 'o': 1},
#     'everyone': {'e': 3, 'v': 1, 'r': 1, 'y': 1, 'o': 1, 'n': 1}
# }

text = "hello everyone"
occurrences_dict = {
    word: {char: word.count(char) for char in word}
    for word in text.split()
}
print(occurrences_dict)

# Write a nested list comprehension to transpose a 3x3 matrix (switch its rows
# and columns).
matrix = [
    [4, 6, 8],
    [0, 0, 0],
    [1, 2, 3],
]

transposed_matrix = [[matrix[i][j] for i in range(3)] for j in range(3)]
print(transposed_matrix)
