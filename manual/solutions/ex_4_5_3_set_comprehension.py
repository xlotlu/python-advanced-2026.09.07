# Write a set comprehension to get all lowercase words in a text.

text = "Write a set comprehension to get all lowercase words in a text"
words = {word.lower() for word in text.split()}
print(words)
