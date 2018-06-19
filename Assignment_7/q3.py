# Python program to find the multiplication table (from 1 to 10) of a number input by the user
def multiplication_table(n, t=1):
    if t == 11:
        return False
    else:
    	print(n * t)
    	multiplication_table(n, t+1)

n = int(input("Enter the number you want multiplication table of: "))
multiplication_table(n)