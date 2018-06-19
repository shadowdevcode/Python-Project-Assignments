'''Write a function to calculate power of a number raised to other ( a^b ) using recursion'''
def power_recursion(base, exp):
	if exp == 1:
		return base
	else:
		return (base * power_recursion(base, exp-1))
base = int(input("Enter base value: "))
exp = int(input("Enter exponential value: "))
print("Result is: ", power_recursion(base, exp))
