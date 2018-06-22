a = 3
try:
    if a < 4:
        a = a / (a - 3)
        print(a)
except:
    print("No error now. Because it is handled now!!")
