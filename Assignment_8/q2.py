# Importing datetime library in python
import datetime

now = datetime.datetime.now()
# Printing the formatted time using strftime function.
print("Formatted time is: ", now.strftime("%Y-%m-%d %H:%M:%S"))