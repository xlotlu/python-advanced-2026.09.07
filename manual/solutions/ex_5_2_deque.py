from collections import deque
# Use deque to implement a simple queue for a movie theater. Run the following
# changes and print the queue after each of them:
# Add customers to the queue in the order they arrive: Alice, Bob, and Charlie.
# Alice can't decide which movie she wants to see, so the clerk sends her back
# to the end of the queue.
# Bob buys his ticket and leaves the queue.
# Another customer, David, joins the queue.

movie_queue = deque()
print(movie_queue)

print("Add customers to the queue in the order they arrive: Alice, Bob, and "
      "Charlie.")
movie_queue.append("Alice")
movie_queue.append("Bob")
movie_queue.append("Charlie")
print(movie_queue)

print("Alice can't decide which movie she wants to see, so the clerk sends her "
      "back to the end of the queue.")
movie_queue.rotate(-1)
print(movie_queue)

print("Bob buys his ticket and leaves the queue.")
movie_queue.popleft()
print(movie_queue)

print("Another customer, David, joins the queue.")
movie_queue.append("David")
print(movie_queue)


# Write a generator function that receives two required parameters: an iterable
# of integers and an integer size. The function should yield the maximum value
# in each sliding window of size size in the iterable. E.g. for iterable =
# [3, 6, 8, 2, 6, 2, 3, 5, 7], size=3 should yield 8, 8, 8, 6, 6, 5, 7

def get_max(iterable, window_size):
    window = deque(maxlen=window_size)

    for item in iterable:
        window.append(item)
        if len(window) == window_size:
            yield max(window)


for window_max in get_max([3, 6, 8, 2, 6, 2, 3, 5, 7], 3):
    print(window_max)
print()


def get_max_v2(iterable, window_size):
    window = deque(maxlen=window_size)

    items = iter(iterable)

    for _ in range(window_size-1):
        window.append(next(items))

    for item in items:
        window.append(item)
        yield max(window)


for window_max in get_max_v2([3, 6, 8, 2, 6, 2, 3, 5, 7], 3):
    print(window_max)