__author__ = 'zile'

'''
Events are a form of asynchronous communication between Greenlets.
'''

import gevent
from gevent.event import Event

evt = Event()

def setter():
    '''After 3 seconds, wake all threads waiting on the value of evt'''
    print('SETTER is doing something!')
    gevent.sleep(3)
    print("SETTER is done")
    evt.set()

def waiter(id):
    '''After 3 seconds the get call will unblock'''

    print("WAITER %s is waiting on you!" %id)
    evt.wait()  # blocking
    print("WAITER %s is gone!" %id)

def main():
    gevent.joinall([
        gevent.spawn(setter),
        gevent.spawn(waiter, 1),
        gevent.spawn(waiter, 2),
        gevent.spawn(waiter, 3),
        gevent.spawn(waiter, 4),
        gevent.spawn(waiter, 5)
    ])

if __name__ == "__main__":
    main()

# SETTER is doing something!
# WAITER 1 is waiting on you!
# WAITER 2 is waiting on you!
# WAITER 3 is waiting on you!
# WAITER 4 is waiting on you!
# WAITER 5 is waiting on you!
# SETTER is done
# WAITER 4 is gone!
# WAITER 1 is gone!
# WAITER 2 is gone!
# WAITER 5 is gone!
# WAITER 3 is gone!