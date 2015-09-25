__author__ = 'zile'


import threading
import time
import random

# create mutex object
lock = threading.Lock()

class MyThread1(threading.Thread):
    def run(self):
        global lock
        print("T1 is sleeping")
        time.sleep(random.randint(6,10))
        print("T1 should finish first!")
        lock.release()

class MyThread2(threading.Thread):
    def run(self):
        global lock
        print("T2 is sleeping")
        time.sleep(random.randint(1,5))
        lock.acquire()
        print("T2 should finish last!")

def main():
    lock.acquire()
    m1 = MyThread1()
    m1.start()
    m2 = MyThread2()
    m2.start()

if __name__ == "__main__":
    main()