user_set1 = set()
user_set1.add(input("Enter elements for set: "))
print(user_set1)

user_set2 = set()
user_set2.add(input("Enter elements for set: "))
print(user_set2)

user_set3 = user_set1 - user_set2
print(user_set3)

user_set1 == user_set2

user_set4 = user_set1 & user_set2
print(user_set4)