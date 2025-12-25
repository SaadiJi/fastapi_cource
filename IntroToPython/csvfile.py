
# with open("names.csv") as file:
#     for line in file:
#         row = line.rstrip().split(",")
#         print(f"{row[0]} is in {row[1]}")
        
# with open("names.csv") as file:
#     for line in file:
#         name,house = line.rstrip().split(",")
#         print(f"{name} is in {house}")

# students = []
# with open("names.csv") as file:
#     for line in file:
#         name,house = line.rstrip().split(",")
#         # student = {}
#         # student["name"] = name
#         # student["house"] = house
#         student = {"name":name, "house":house}
#         students.append(student)

# def get_name(student):
#     return student["name"]

# for student in sorted(students,key=get_name,reverse=True):
#     print(f"{student['name']} is in {student['house']}")
import csv

# students = []
# with open("names.csv") as file:
#     reader = csv.reader(file)
#     for name, home in reader:
#         students.append({"name":name, "home":home})

# for student in sorted(students,key=lambda student: student["name"]):
#     print(f"{student['name']} is in {student['home']}")

# students = []
# with open("names.csv") as file:
#     reader = csv.DictReader(file)
#     for row in reader:
#         students.append({"name":row["name"], "home":row["home"]})

# for student in sorted(students,key=lambda student: student["name"]):
#     print(f"{student['name']} is in {student['home']}")
    
import csv

name = input("what your name? ")
home = input("where your home? ")

with open("names.csv", "a") as file:
    writer = csv.DictWriter(file, fieldnames=["name","home"])
    writer.writerow({"home":home,"name":name})