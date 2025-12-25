students = ["Hermione", "Harry", "Ron"]
# gryffindors = [{"name": student, "house": "Gryffindors"} for student in students]
gryffindors = {student: "Gryffindor" for student in students}
print(gryffindors)