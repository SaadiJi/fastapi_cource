students = [
    {"name": "Hermione", "house": "Gryffindor"},
    {"name": "Harry", "house": "Gryffindor"},
    {"name": "Ron", "house": "Gryffindor"},
    {"name": "Draco", "house": "Slytherin"},
]

# list comprehension
# gryffindors = [
#     student["name"] for student in students if student["house"] == "Gryffindor"
# ]

# for gryffindor in sorted(gryffindors):
#     print(gryffindor)

#filter
# def is_gryffindor(s):
#     return s["house"] == "Gryffindor"

# gryffindors = filter(is_gryffindor, students)

# for gryffindor in sorted(gryffindors, key=lambda gryffindor: gryffindor["name"]):
#     print(gryffindor["name"])

#filter 2
gryffindors = filter(lambda gryffindor: gryffindor["house"], students)

for gryffindor in sorted(gryffindors, key=lambda gryffindor: gryffindor["name"]):
    print(gryffindor["name"])