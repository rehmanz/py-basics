'''
Created on Jul 7, 2014

@author: zrehman
'''
from time import sleep
from Queue import Queue
from threading import Thread
import time

q = Queue()
workers = []
concurrency = 3

def worker():
    print '\n'
    while True:
        line = q.get()
        print "processing: %s\n" % line
        time.sleep(1)
        q.task_done()

for i in range(concurrency):
    t = Thread(target=worker)
    t.setDaemon(True)
    workers.append(t)
    t.start()

# There are generic commands and not tasks but testing concurrency logic
tasks_l = ['ls', 'ps -ef', 'pwd', 'whoami', 'ls', 'ps -ef', 'pwd', 'whoami']
for task in tasks_l:
    q.put(task)

print 'Done reading!'
q.join()