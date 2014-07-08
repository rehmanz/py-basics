'''
Created on Jul 6, 2014

@author: zrehman
'''
##
# Compare two dictionaries of any types
##

def is_dict(e):
    return isinstance(e, dict)

def compare_dictionaries(d1, d2):
    # Type checking
    if not (is_dict(d1) and is_dict(d2)):
        raise ValueError('Type mismatch: d1=%s != d2=%s' %(type(d1), type(d2)))
    else:
        return d1 == d2

d1 = {'x' : 1,
      'y' : 2,
      'a1' : [1, 2, {'k' : 10, 'm' : 500}]}
d2 = {'x' : 1,
      'y' : 2,
      'a1' : [1, 2, {'k' : 10, 'm' : 500}]}
d3 = {'foo' : 'bar'}
print compare_dictionaries(d1, d2)
print compare_dictionaries(d1, d3)



"""
>>> def is_dict(e):
...     return isinstance(e, dict)
... 
>>> def compare_dictionaries(d1, d2):
...     # Type checking
...     if not (is_dict(d1) and is_dict(d2)):
...         raise ValueError('Type mismatch: d1=%s != d2=%s' %(type(d1), type(d2)))
...     else:
...         return d1 == d2
... 
>>> d1 = {'x' : 1,
...       'y' : 2,
...       'a1' : [1, 2, {'k' : 10, 'm' : 500}]}
>>> d2 = {'x' : 1,
...       'y' : 2,
...       'a1' : [1, 2, {'k' : 10, 'm' : 500}]}
>>> d3 = {'foo' : 'bar'}
>>> print compare_dictionaries(d1, d2)
True
>>> print compare_dictionaries(d1, d3)
False
>>> 

"""