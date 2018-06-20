import threading
import time

def displaylist(threadname, elem, delay):
    """thread display list function"""
    counter = 0
    while counter < 6:
        time.sleep(delay)
        counter += 1
        print("%s: %s: %d" % (threadname, time.ctime(time.time()), elem))

threadlist = []

for i in range(5):
    t = threading.Thread(target=displaylist, args=(i,))
    threadlist.append(t)
    t.start()