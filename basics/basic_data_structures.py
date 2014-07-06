'''
Created on Jul 6, 2014

@author: zrehman
'''
##
# Stacks (LIFO)
##
stack = [3, 4, 5]

# Push Operation
stack.append(6)
stack.append(7) # [3, 4, 5, 6, 7]

# Pop Operation
stack.pop()     # [3, 4, 5, 6]
"""
>>> stack = [3, 4, 5]
>>> 
>>> # Push Operation
... stack.append(6)
>>> stack.append(7) # [3, 4, 5, 6, 7]
>>> 
>>> # Pop Operation
... stack.pop()     # [3, 4, 5, 6]
7
"""

##
# Queues (FIFO)
##
from collections import dequeue
q = deque(['task1', 'task2', 'task3'])

# Enqueue
q.append('task4')     # ['task1', 'task2', 'task3', 'task4']
q.append('task5')     # ['task1', 'task2', 'task3', 'task4', 'task5']

# Dequeue
q.popleft()            # task1
q.popleft()            # task2

print q                #  ['task3', 'task4', 'task5']

##
# Functional Programming Tools
##
# Find all even numbers in a list using filter
def even(x):return x%2
filter(even, range(1, 10))

# Find the square root of all numbers in the list
import math
map(math.sqrt, range(1, 10))

# reduce(function, sequence) returns a single value by calling bin function on first two items in sequence
def add(x, y): return x+y
reduce(add, range(1, 11)

##
# List Comprehension
##
# Each element in a list is a result of an operation
squares = [x**2 for x in range(10)]
squares = map(lambda x: x**2, range(10))
"""
"""

# Nested List
"""
>>> def exists(client): return r.exists(client)
... 
>>> clients = ['Host1', 'Host2']
>>> map(exists, clients)
[True, False]
>>> map(exists, clients)
[True, False]
>>> map(exists, clients)
[True, False]
>>> all(map(exists, clients))
False
>>> all(map(exists, clients))
True
"""
