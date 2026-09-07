# Create a dict {"a": 97, "b": 98, ... } using comprehension. Use ord built-in
# to obtain ASCII code and string.ascii_lowercase to get all letters.
import string

ascii_dict = {char: ord(char) for char in string.ascii_lowercase}
print(ascii_dict)

# Using the dictionary generated above, create another one where you swap keys
# and values.
swapped_dict = {value: key for key, value in ascii_dict.items()}
print(swapped_dict)

# Filter the above dictionary to contain only even keys.
filtered_dict = {key: val for key, val in swapped_dict.items() if key % 2 == 0}
print(filtered_dict)
