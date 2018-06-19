quantity = int(input("Enter quantity for user: "))
unit = 100
cost_purchased_quantity = (quantity * unit)
print(cost_purchased_quantity)
if (cost_purchased_quantity > 1000):
	total_cost = (10 * cost_purchased_quantity)/100 + cost_purchased_quantity
	print("Total Cost: ", total_cost)
else:
	print("No discount will be given", cost_purchased_quantity)