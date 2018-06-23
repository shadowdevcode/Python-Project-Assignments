# Write a Python program to write 10 random numbers into a file.
# Read the file and then sort the numbers and then store it to another file.

import random   # In Order to generate a series of random numbers we use random
try:
    with open("random.txt", "w") as f:
        for i in range(10):
            line = str(random.randint(1, 100))  # Generate a series from 1 - 100
            f.writelines(line + '\n')
            print(line)

    with open("random.txt") as f1, open("random1.txt", "w") as f2:
            lines = f1.read().splitlines()
            lines.sort()    # Using sort numbers are getting sorted in the file.

    for i in lines:
        f2.write(str(i))
except ValueError:  # handled ValueError raised while running this operation.
    print("Removed Value Error")
