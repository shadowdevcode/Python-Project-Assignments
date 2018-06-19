student = {}
while len(student) < 10:
	name = input("Enter Name of the student: ")
	marks = int(input("Enter marks of the student: "))
	student[name] = marks
print(student)