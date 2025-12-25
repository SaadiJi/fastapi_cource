# import random
# class Hat:
#     def __init__(self):
#         self.houses = ["Lahore", "Karachi", "Sargodha", "Multan"]
#     def sort(self, name):
#         print(name, "is in", random.choice(self.houses))    
    
    
# hat = Hat()
# hat.sort("Harry")


# import random
# class Hat:
#     houses = ["Lahore", "Karachi", "Sargodha", "Multan"]
#     @classmethod
#     def sort(cls, name):
#         print(name, "is in", random.choice(cls.houses))    
    
    
# Hat.sort("Harry")

# class Student:
#     def __init__(self, name, house):
#         self.name = name
#         self.house = house
        
#     def __str__(self):
#         return f"{self.name} from {self.house}"
    
#     @classmethod
#     def get(cls):
#         name = input("Name : ")
#         house = input("House : ")
#         return cls(name, house)
    
# def main():
#     student = Student.get()
#     print(student)
    
# if __name__ == "__main__":
#     main()


class Wizard:
    def __init__(self,name):
        self.name = name

class Student(Wizard):
    def __init__(self, name, house):
        super().__init__(name)
        self.house = house

class Professor(Wizard):
    def __init__(self, name, subject):
        super().__init__(name)
        self.subject = subject
        
wizard = Wizard("Saadi")
student = Student("Bilal", "Lahore")
professor = Professor("Hashim", "Chemistry")