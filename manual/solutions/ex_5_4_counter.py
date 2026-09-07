from collections import Counter

# Use a Counter to count the frequency of each word in a sentence.

text = """Beautiful is better than ugly
Explicit is better than implicit"""

word_counter = Counter(text.lower().split())
print(word_counter)
