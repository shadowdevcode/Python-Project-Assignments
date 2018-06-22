# Write a program to show and handle following exceptions:
# 1. Import Error
# 2. Value Error
# 3. Index Error
import sys
try:
    x = int(input("Enter a number: "))
    from time import datetime
    data = list[2]
except (ValueError, ImportError, IndexError):
    print("Non numeric data found!")
    print("No import module found")
    print("Out of index")


