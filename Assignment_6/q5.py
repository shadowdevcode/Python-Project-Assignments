even_numbers = []
odd_numbers = []
for i in range(1,101):	
	if (i % 2 == 0):
		even_numbers.append(i)
	else:
		odd_numbers.append(i)
print("List of Even Numbers: ", even_numbers)
print("List of Odd Numbers: ", odd_numbers)
