# Write a function filter_short_words(word_list, n) that returns the words in
# word_list shorter than n. Use filter built-in function and a lambda function.
import operator


def filter_short_words(word_list, n):
    return list(filter(lambda word: len(word) < n, word_list))


words = ["function", "test", "parameter", "class", "list"]
print("Words in", words, "shorter than 6 characters:",
      filter_short_words(words, 6))

# Write a function that takes a list of tuples, where each tuple contains two
# integers, and returns a new list containing the product of the two integers
# in each tuple. Use the map function and a lambda function to implement this.
tuples = [(4, 5), (13, 6), (75, 2), (54, 11), (84, 3)]


def product_of_tuples(tuple_list):
    return list(map(lambda tup: tup[0] * tup[1], tuple_list))


print(f"Products of tuples' elements: input={tuples}, "
      f"output={product_of_tuples(tuples)}")


# Write a function that receives any number of strings and returns the list of
# unique strings ordered by number of appearances (most frequent → least
# frequent). Use sorted built-in function.
#
# E.g. f('hello', 'there', 'hello', 'hi', 'hi', 'hello') ->
# ['hello', 'hi', 'there']
def sort_words(*words):
    return sorted(set(words), key=words.count, reverse=True)


str_list = ['hello', 'there', 'hello', 'hi', 'hi', 'hello', 'bye']
print(f"Words in {str_list} from most frequent to least frequent:")
for elem in sort_words(*str_list):
    print(elem)


# Write your own implementation for map function (or any other function
# mentioned above).
def my_map(function, iterable, /):
    for item in iterable:
        yield function(item)


for cap_word in my_map(str.upper, words):
    print(cap_word)
