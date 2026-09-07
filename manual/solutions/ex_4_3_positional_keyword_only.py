# Write a function that takes any number of strings and an integer min_length as
# parameters. min_length should be an optional keyword-only parameter. Return
# the list of strings longer than min_length. By default (when min_length not
# given), it should return a list containing all words.

def get_long_words(*words, min_length=-1):
    long_words = []
    for word in words:
        if len(word) > min_length:
            long_words.append(word)
    return long_words


def get_long_words_v2(*words, min_length=-1):
    return [word for word in words if len(word) > min_length]


print(get_long_words("hello", "hi", "world", "bye", min_length=3))
print(get_long_words("hello", "hi", "world", "bye", ""))
print(get_long_words(min_length=5))

print(get_long_words_v2("hello", "hi", "world", "bye", min_length=3))
print(get_long_words_v2("hello", "hi", "world", "bye", ""))
print(get_long_words_v2(min_length=5))


# Write a function calculate_total that accepts positional-only arguments for
# price and quantity, and a keyword-only argument discount with a default value
# of 0. The function should return the total price after applying the discount.

def calculate_total(price, quantity, /, *, discount=0):
    return price * quantity - discount


print(calculate_total(15, 3))
print(calculate_total(15,3, discount=7))
