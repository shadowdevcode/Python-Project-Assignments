age1 = int(input("Enter age of first person: "))
age2 = int(input("Enter age of second person: "))
age3 = int(input("Enter age of third person: "))
list1 = []
list1.append(age1)
list1.append(age2)
list1.append(age3)
print("Oldest age of person: ", max(list1))
print("Youngest age of person: ", min(list1))