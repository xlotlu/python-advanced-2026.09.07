# Create a generator function that receives a parameter max_nr and yields a
# random number between 1 and max_nr, indefinitely. From outside, iterate it
# in a loop that stops after 10 cycles.
import os
import random


def infinite_random(max_nr):
    while True:
        yield random.randint(1, max_nr)


rand = infinite_random(100)
for i in range(10):
    print(next(rand))


# Write a generator function that yields unique elements from an iterable
# received as parameter.
def generate_unique(iterable, /):
    unique = []
    for item in iterable:
        if item in unique:
            continue

        unique.append(item)
        yield item


unique_gen = generate_unique([[1, 2], [1, 1], [1, 1], [2, 2], [1, 2]])
for nr in unique_gen:
    print(nr)


# Write a generator function that takes a path and a file extension as
# positional-only arguments (both as strings), and a boolean recursive as
# keyword-only argument. The function will yield all files with the extension
# extension in path; if recursive is true, if will also search inside
# subdirectories of path. Use os.walk or glob.iglob.
import glob
from pathlib import Path


def find(path, extension, /, *, recursive=False, include_hidden=False):
    pattern = Path(path)

    if recursive:
        pattern /= "**"

    pattern /= f"*.{extension}"
    return glob.iglob(
        str(pattern),
        recursive=recursive,
        include_hidden=include_hidden,
    )


print("All .py files in the project, excluding hidden files (recursively)")
for filename in find("..", "py", recursive=True):
    print(filename)

print("All .py files in the project (recursively)")
for filename in find("..", "py", recursive=True, include_hidden=True):
    print(filename)

print("All .py files in the current directory")
for filename in find(".", "py"):
    print(filename)


def find_os_walk(path, extension, /, *, recursive=False):
    for dir_path, _, files in os.walk(path):
        for file in files:
            if file.endswith(f".{extension}"):
                yield os.path.join(dir_path, file)
        if not recursive:
            break


print("All .py files in the project (recursively)")
for filename in find_os_walk("..", "py", recursive=True):
    print(filename)

print("All .py files in the current directory")
for filename in find_os_walk(".", "py"):
    print(filename)


def find_pathlib_walk(path, extension, /, *, recursive=False):
    path = Path(path)
    for dir_path, _, files in path.walk():
        for file in files:
            if file.endswith(f".{extension}"):
                yield dir_path / file
        if not recursive:
            break


print("All .py files in the project (recursively)")
for filename in find_pathlib_walk("..", "py", recursive=True):
    print(filename)

print("All .py files in the current directory")
for filename in find_pathlib_walk(".", "py"):
    print(filename)