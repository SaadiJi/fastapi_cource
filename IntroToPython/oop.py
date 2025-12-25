

# def main():
    # name, house = get_student()
    # print(f"{name} from {house}")
    # student = get_student()
    # if student[0] == "Saadi":
    #     student[1] = "Sargodha"
    # print(f"{student[0]} from {student[1]}")
    # student = get_student()
    # if student["name"] == "Saadi":
    #     student["house"] = "Sargodha"
    # print(f"{student['name']} from {student['house']}")
   
# def get_student():
#     name = input("Name: ")
#     house = input("House: ")
#     # return name,house   #tuple immutable (could not changed)
#     # return (name,house) #tuple immutable (could not changed)
#     # return [name,house] #List mutable (could changed)
#     return {"name":name, "house":house} #dictnory mutable (could changed)


class Student:
    def __init__(self, name, house):
        if not name:
            raise ValueError("Missing Name")
        if house not in ["Lahore", "Sargodha", "Karachi", "Faisalabad"]:
            raise ValueError("Invalid House")
        self.name = name
        self.house = house
        
    def __str__(self):
        return f"{self.name} from {self.house}"
    
    
def main():
    student = get_stude_2()
    print(student)
    # print(f"{student.name} from {student.house}")
  
  
def get_stude():
    student = Student()
    student.name = input("Name: ")
    student.house = input("House: ")
    return student

def get_stude_2():
    name = input("Name: ")
    house = input("House: ")
    student = Student(name,house)
    return student

if __name__ == "__main__":
    main()