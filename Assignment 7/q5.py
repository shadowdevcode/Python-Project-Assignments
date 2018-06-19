'''Write a function to find factorial of a number but also store the factorials calculated in a dictionary'''
num = int(input("Enter the number for factorial: "))
def factorial(n):
   if n == 1:
       return n
   else:
       return n*factorial(n - 1)
fact = factorial(num)
print(fact)
dict={
   num:fact
}
print(dict)
