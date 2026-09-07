# Write a program that saves user inputs in a list. The program stop asking the
# user to enter a word when the user doesn't enter anything (presses Enter).
user_inputs = []
while user_input := input("Enter something: "):
    user_inputs.append(user_input)

print(user_inputs)


# Open and parse users.json using json. Save the result in a Python variable.
# Iterate over users and, for each user that is between 25 and 50 years old
# (including the limits) and has a name (key name), display a message:
# User <name> is <age> years old.
import json
from pathlib import Path


users_path = Path.cwd().parent / "docs" / "users.json"
with users_path.open() as f:
    users = json.load(f)
    for user in users:
        if (name := user.get("name")) and 25 <= (age := user.get("age", 0)) <= 50:
            print(f"User {name} is {age} years old.")
