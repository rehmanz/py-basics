'''
Created on Jul 6, 2014

@author: zrehman
'''
import re

str = '<configure_host_state.ConfigureHostState instance at 0x106fc8a70>'

# Compile a regexp
regexp = re.compile('^<\w+\.ConfigureHostState instance.*')

# Test and store result
result = regexp.match(str)

"""
>>> import re
>>> 
>>> str = '<configure_host_state.ConfigureHostState instance at 0x106fc8a70>'
>>> 
>>> # Compile a regexp
... regexp = re.compile('^<\w+\.ConfigureHostState instance.*')
>>> 
>>> print regexp.match(str)
<_sre.SRE_Match object at 0x101ef8ed0>
>>> result = regexp.match(str)
"""