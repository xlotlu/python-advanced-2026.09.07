# Write a function normalize that receives a string as a parameter and returns
# the string modified as follows:
# any trailing whitespace is removed
# any trailing punctuation is removed (you can use string.punctuation)
# the string is transformed to all lowercase
import string


def normalize(text):
    return text.strip().strip(string.punctuation).lower()


print(normalize("  HELLO world!!"))
print(normalize("  Hello World..\n"))
