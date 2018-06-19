a=[]
c=[]
count_even=0
count_odd=0
n1=int(input("Enter number of elements:"))
for i in range(n1):
    b=int(input("Enter element for b:"))
    a.append(b)
n2=int(input("Enter number of elements:"))
for i in range(n2):
    d=int(input("Enter element for d:"))
    c.append(d)
new=a+c
new.sort()
print("Sorted list is:",new)

for i in new:
	if(i%2==0):
		count_even+=1
	else:
		count_odd+=1
print("Even Number :",count_even)
print("Odd Number :",count_odd)	