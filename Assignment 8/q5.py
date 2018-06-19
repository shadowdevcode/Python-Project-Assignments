# Using datetime and time library
import datetime
import time

now = datetime.datetime.now().strftime("%d/%m/%Y")
# Extracting from date and time - day using strftime
print("Extracted day: ", datetime.datetime.now().strftime("%d"))