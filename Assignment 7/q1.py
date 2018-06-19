# Create a function to calculate the area of a circle by taking radius from user.
PI = 3.142
area = 0
def area_circle(r):
	return (PI * r * r)
r = int(input("Enter the radius of the circle: "))
print("Area of circle is %.6f " % area_circle(r))
