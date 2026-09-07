# Write a function called calculate_average that takes in any number of
# arguments and calculates their average. The function should accept integers
# and floats. If no arguments are provided, the function should return 0. If
# arguments are provided, the function should calculate their average and return
# it rounded to two decimal places.

def calculate_average(*numbers):
    if not numbers:
        return 0
    avg = round(sum(numbers) / len(numbers), 2)
    return avg


print(calculate_average())
print(calculate_average(1, 3.6643, 67, 8.5, 5.3))


# Write a function process_order that accepts keyword arguments representing
# items and their quantities. The function should calculate the total number of
# items ordered and print a summary.
#
# E.g.
#
# process_order(apples=5, bananas=3, oranges=2)
# should output:
#
# You have ordered:
# apples: 5
# bananas: 3
# oranges: 2
# Total items: 10

def process_order(**items):
    if not items:
        print("You haven't ordered anything")
        return

    items_count = 0
    print("You have ordered:")
    for item, count in items.items():
        print(f"{item}: {count}")
        items_count += count
    print(f"Total items: {items_count}")


process_order()
process_order(apples=5, bananas=3, oranges=2)
