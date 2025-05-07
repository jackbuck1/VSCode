class student:
    def __init__(self, name, age, classroom):
        self.name = name
        self.age = age
        self.classroom = classroom

name1 = input ("Please enter your name: ")
age1 = int(input("Please enter your age: "))
classroom1 = input ("Please enter your classroom: ")

name2 = input ("Please enter your name: ")
age2 = int(input("Please enter your age: "))
classroom2 = input ("Please enter your classroom: ")

student1 = student(f"{name1},{age1}, {classroom1}")
student2 = student(f"{name2},{age2}, {classroom2}")

print(student1.classroom1)