__author__ = 'zile'

'''
Queues are ordered sets of data that have the usual put / get operations but are written in a way such that they can
be safely manipulated across Greenlets.

For example if one Greenlet grabs an item off of the queue, the same item will not be grabbed by another Greenlet
executing simultaneously.
'''

import gevent
from gevent.queue import Queue

tasks = Queue()
counter = 1

def worker(n):
    while not tasks.empty():
        task = tasks.get()
        print('WORKER %s got task %s' % (n, task))
        gevent.sleep(0) # important to place so a worker greenlet can yield to other worker
        print('WORKER %s doing work %s' % (n, task))


    print('Quitting time!')

def boss():
    for i in xrange(1,25):
        tasks.put_nowait(i)

gevent.spawn(boss).join()

def main():
    gevent.joinall([
        gevent.spawn(worker, 'Steve'),
        gevent.spawn(worker, 'John'),
        gevent.spawn(worker, 'Nancy'),
    ])

if __name__ == "__main__":
    main()

# WORKER Steve got task 1
# WORKER John got task 2
# WORKER Nancy got task 3
# WORKER Steve got task 4
# WORKER John got task 5
# WORKER Nancy got task 6
# WORKER Steve got task 7
# WORKER John got task 8
# WORKER Nancy got task 9
# WORKER Steve got task 10
# WORKER John got task 11
# WORKER Nancy got task 12
# WORKER Steve got task 13
# WORKER John got task 14
# WORKER Nancy got task 15
# WORKER Steve got task 16
# WORKER John got task 17
# WORKER Nancy got task 18
# WORKER Steve got task 19
# WORKER John got task 20
# WORKER Nancy got task 21
# WORKER Steve got task 22
# WORKER John got task 23
# WORKER Nancy got task 24
# Quitting time!
# Quitting time!
# Quitting time!