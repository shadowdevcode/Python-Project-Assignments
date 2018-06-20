import _thread

import time

def print_thread(threadname, delay = 5):

    counter = 0
    while counter < 3:
        time.sleep(delay)
        counter += 1
        print("%s: %s" % (threadname, time.ctime(time.time())))

try:
    _thread.start_new_thread(print_thread, ("Thread-1", ))

except:

    print("Error: Unable to start thread")

while 1:
    pass



