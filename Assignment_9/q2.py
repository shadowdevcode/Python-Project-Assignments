class Student:

    def __init__(self):
        self.name = input("Enter name of the student: ")
        self.rollnumber = int(input("Enter roll number: "))

    def display(self):
        print("Student's name is: " + self.name)
        print("Student's roll number: ", self.rollnumber)

s = Student()
s.display()
