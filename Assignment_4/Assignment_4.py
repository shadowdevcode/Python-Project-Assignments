tuple1 = ('python', 2, 'name', 4.5)
print(len(tuple1))

list = []
num1 = int(input("How many numbers to check: "))

for i in range(num1):
	num2 = int(input("Enter the number: "))
	list.append(num2)

print(list)
print(tuple(list))
print("Maximum element in the above list is: ", max(list))
print("Minimum element in the above list is: ", min(list))


def multiplyList(myList) :
     
    # Multiply elements one by one
    result = 1
    for x in myList:
         result = result * x 
    return result 
     
list1 = []
list2 = []
zen = int(input("Enter the total no of entries: ")) 
for i in range(zen):
	x = int(input("Enter number for list 1: "))
	list1.append(x) 
print(tuple(list1))

for j in range(zen):
	y = int(input("Enter number for list 2: "))
	list2.append(y) 
print(tuple(list2))

print(multiplyList(list1))
print(multiplyList(list2))