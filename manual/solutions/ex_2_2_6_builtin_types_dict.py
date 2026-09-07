# Write a function invert_dict that inverts a dictionary, i.e., the keys become
# values and the values become keys. Handle cases where values are not unique by
# storing the keys in a list.

def invert_dict(d):
    new_dict = {}
    for key, value in d.items():
        if value not in new_dict:
            new_dict[value] = [key]
        else:
            new_dict[value].append(key)
    return new_dict


print(invert_dict({"name": "Alice", "age": 25, "num_friends": 25}))
