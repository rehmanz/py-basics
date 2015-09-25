__author__ = 'zile'

'''
An extension of the Event object is the AsyncResult which allows you to send a value along with the wakeup call.
This is sometimes called a future or a deferred, since it holds a reference to a future value that can be set on an
arbitrary time schedule.
'''

import gevent
from gevent.event import AsyncResult

a = AsyncResult()
d

def setter():
    """
    After 3 seconds set the result of a.
    """
    gevent.sleep(3)
    a.set('SETTER says hello!')

def waiter(id):
    """
    After 3 seconds the get call will unblock after the setter
    puts a value into the AsyncResult.
    """
    print('WAITER #%s is waiting for results' %id)
    print("WAITER #%s got \"%s\"" %(id, a.get()))

def main():
    gevent.joinall([
        gevent.spawn(setter),
        gevent.spawn(waiter, 1),
        gevent.spawn(waiter, 2),
        gevent.spawn(waiter, 3),
        gevent.spawn(waiter, 4),
    ])

if __name__ == "__main__":
    main()