list1 = list(range(9))
#Created a list of numbers and an empty list too. 
#Calculated square of elements in list1 and stored in new empty list
list2 = []
for i in list1:
	j = i**2	
	print(j)
	list2.append(j)
print(list2)