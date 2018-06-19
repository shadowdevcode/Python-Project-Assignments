# Using datetime library
import datetime

now = datetime.datetime.now()
# Extracting from date and time - month using strftime
print("Extracted month: ", now.strftime("%m"))