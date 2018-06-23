# Output

# Zero Division Error - division by zero

a = 3
try:
    if a < 4:
        a = a / (a - 3)  # throws ZeroDivisionError for a = 3
        print(a)
except:
    print("No error now. Because it is handled now!!")
