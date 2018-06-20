import _thread

import time

def print_thread(threadname, delay):

    num_count = 0
    while num_count < 11:
        time.sleep(delay)
        num_count += 1
        print("%s: %s: %d" % (threadname, time.ctime(time.time()), num_count))

try:
    _thread.start_new_thread(print_thread, ("Number List:", 1))

except:

    print("Error: Unable to start thread")

while 1:
    pass
