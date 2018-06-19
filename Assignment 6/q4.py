# From a list containing ints, strings and floats, make three lists to store them separately 
list1 = [1, 'a', 'b', 'c', 2, 2.3, 6.7, 't', 5]
list2 = [i for i in list1 if isinstance(i, int)]
print(list2)
list3 = [i for i in list1 if isinstance(i, str)]
print(list3)
list4 = [i for i in list1 if isinstance(i, float)]
print(list4)
# Tried with test cases.
# for i in list1:	
# 	print(i)
# 	if isinstance(i, int):	
# 		list2.append(i)
# 		print("List of Integers : ", list2)
