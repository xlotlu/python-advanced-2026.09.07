from collections import OrderedDict

# Implement a simple Least Recently Used (LRU) cache using OrderedDict
# (most recent items will be at the end).
# Create an OrderedDict to act as an LRU cache; consider its maximum size to be
# 3
# Create a helper function to add an item to the LRU cache:
# if the item is already in the cache, move it to the end of the cache
# update the value for the item
# if maximum size is exceeded, remove the oldest item
# Add multiple values to the cache and inspect its value between operations.

cache = OrderedDict()
MAX_SIZE = 3


def add_to_cache(key, value):
    if key in cache:
        cache.move_to_end(key)
    cache[key] = value
    if len(cache) > MAX_SIZE:
        cache.popitem(last=False)


if __name__ == "__main__":
    add_to_cache("test", 100)
    print(cache)

    add_to_cache("hello", 20)
    print(cache)

    add_to_cache("world", 30)
    print(cache)

    add_to_cache("new", 0)
    print(cache)  # test is removed

    add_to_cache("hello", 50)
    print(cache)  # hello is moved to end
