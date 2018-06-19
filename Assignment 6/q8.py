#Take inputs from user to make a list. 
#Again take one input from user and search it in the list and delete that element, if found. 
#Iterate over list using for loop.
new_list = []
for i in range(5):	
	element = int(input("Enter the number : "))
	new_list.append(element)
print(new_list)
num1 = int(input("Enter the number you want to search: "))
for i in range(len(new_list)):	
	if i == num1:
		new_list.remove(num1)
print("Number is matched. Hence deleted list is: ", new_list)
	