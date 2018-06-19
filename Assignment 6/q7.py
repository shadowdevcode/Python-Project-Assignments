#Create a user defined dictionary and get keys corresponding to the value using for loop.
my_dict = {}
for x in range(2):
	new_key = input('Enter name : ')
	new_value = input('Enter age : ')
	my_dict[new_key] = new_value
print(my_dict)
for new_key, new_value in my_dict.items():	
	print(new_value, new_key)
# for key, value in my_dict.items(): # returns the dictionary as a list of value pairs -- a tuple.
#     print (key, value)