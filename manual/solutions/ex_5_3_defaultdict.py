from collections import defaultdict

# Given a list of (student, grade) tuples, group the students by their grades.
# E.g. students = [("Alice", 9), ("Charlie", 7), ("Jane", 9), ("David", 10),
# ("Eve", 10)] should return {9: ["Alice", "Jane"], 7: ["Charlie], 10:
# ["David", "Eve"]}

students = [("Alice", 9), ("Charlie", 7), ("Jane", 9), ("David", 10),
            ("Eve", 10)]

grouped_students = defaultdict(list)
for student, grade in students:
    grouped_students[grade].append(student)

print(grouped_students)

# Given a list of (product, category, price) tuples, compute totals per
# category.
items = [
    ("bread", "food", 2),
    ("milk", "food", 1.5),
    ("chair", "furniture", 45),
    ("charger", "electronics", 50),
    ("eggs", "food", 3.8),
    ("desk", "furniture", 180),
]
totals = defaultdict(int)

for _, category, price in items:
    totals[category] += price

print(totals)
