'''
Created on Jul 6, 2014

@author: zrehman
'''
# Using list comprehension, populate x = [0, 2, 4, 6, 8, 10]
max = 6
x = [i*2 for i in range(max)]
"""
>>> max = 6
>>> x = [i*2 for i in range(max)]
>>> x
[0, 2, 4, 6, 8, 10]
"""

# Now store all elements in a dictionary
y = {i: i*2 for i in range(max)}
"""
>>> y = {i: i*2 for i in range(max)}
>>> y
{0: 0, 1: 2, 2: 4, 3: 6, 4: 8, 5: 10}
"""

# Given a string, s = 'Hello World' reverse the order
# Extended slicing: [begin:end:step]
s = 'Hello World'
reverse_s = s[::-1]
"""
>>> reverse_s = s[::-1]
>>> reverse_s
'dlroW olleH'

# or

>>> ''.join(reversed(s))
'drow lufrednow a si sihT'
"""

# Now reverse the word s = 'This is a wonderful word'
s = 'This is a wonderful word'
split_s = s.split(' ')  # ['This', 'is', 'a', 'wonderful', 'word']
split_s.reverse()       # ['word', 'wonderful', 'a', 'is', 'This']
reverse_s = ' '.join(split_s) # 'word wonderful a is This'
#'This is a wonder world. \nAnd full of maddness'

# Now reverse a paragraph p = 'This is a wonder world. \nAnd full of maddness'
p = 'This is a wonder world. \nAnd full of maddness'
reverse_p = ''
for line in p.splitlines():
    split_l = line.split(' ')
    split_l.reverse()
    reverse_p += ' '.join(split_l)
    reverse_p += '\n'
print reverse_p
'''
 world. wonder a is This
maddness of full And
'''