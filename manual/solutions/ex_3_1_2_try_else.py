# Create a function process_file that takes a filename as an argument. If the
# file cannot be open, print a message with the reason. If the file was
# successfully open, print the number of distinct words in the file (word =
# any succession of characters that are not whitespace).

def process_file(filename):
    try:
        with open(filename) as f:
            content = f.read()
    except FileNotFoundError:
        print("File not found:", filename)
    else:
        words = set(content.split())
        print(len(words), "distinct words in", filename)


process_file("../README.md")
process_file("nonexistent.txt")
