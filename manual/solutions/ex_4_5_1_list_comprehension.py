# Write a list comprehension that creates a list of numbers from 1 to 20 that
# are divisible by 3.
div_by_3 = [i for i in range(1, 21) if i % 3 == 0]
print(div_by_3)

# Write a list comprehension that transforms all strings in a list by making
# them all lowercase and by replacing as with *s.
text = "Write a list comprehension that transforms all strings"
censored_words = [word.lower().replace("a", "*") for word in text.split()]
print(censored_words)

# Write a list comprehension that creates a list of all the words in a given
# string that have more than 3 letters.
long_words = [word for word in text.split() if len(word) > 3]
print(long_words)
