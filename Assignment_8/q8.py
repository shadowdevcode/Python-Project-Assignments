# """Used import to import math libraries"""
import math
# User input
num1 = int(input("Enter the smaller number: "))
num2 = int(input("Enter the larger number: "))
# Applied gcd function using math lib
result = math.gcd(num2, num1)  
print("Greatest Common Divisor of a user-input number are = ", result)