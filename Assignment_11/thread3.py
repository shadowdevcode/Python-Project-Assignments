import time
from threading import Thread


def displaylist(i, delay):
        time.sleep(delay)
        print("Thread %d : %s" %((i), time.ctime(time.time())))

a = []
for j in range(5):
    a.append(j)
print(a)
delay = 2

try:

    for i in a:
        thread1 = Thread(target = displaylist, args =(i, delay,))
        thread1.start()
        delay += 2
except:
    print("Error, Thread is not working!")
