# Using datetime library
import datetime

now = datetime.datetime.date()
# Extracting from date and time - day using strftime
print("Extracted day: ", now.strftime("%d"))