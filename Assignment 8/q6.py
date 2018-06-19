# Import time library
import time
# Use of localtime function along with asctime which takes time as attribute
print(time.asctime(time.localtime(time.time())))