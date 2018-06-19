points = int(input("Enter the points scored: "))
if (points < 200):
	if (points > 1) and (points < 50):
		print("Congratulations! You won a No Prize!")
	elif (points > 51) and (points < 150):
		print("Congratulations! You won a Wooden Dog!")
	elif (points > 151) and (points < 180):
		print("Congratulations! You won a Book!")
	elif (points > 181) and (points < 200):
		print("Congratulations! You won a Chocolates!")
	else:
		print("Sorry! No Prize this time")			
else:
	print("Please enter points less than 200")