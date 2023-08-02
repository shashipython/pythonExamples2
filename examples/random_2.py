#To generate numbers in a specific numerical range, use uniform() instead.
import random

for i in xrange(5):
    print '%04.3f' % random.uniform(1, 100)
	
'''
$ python random_uniform.py

6.899
14.411
96.792
18.219
63.386
'''
