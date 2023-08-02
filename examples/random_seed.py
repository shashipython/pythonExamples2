'''
he seed value controls the first value produced by the formula used to produce pseudorandom numbers, and since the formula is deterministic it
also sets the full sequence produced after the seed is changed
'''

import random

random.seed(1)

for i in xrange(5):
    print '%04.3f' % random.random()
	
'''
$ python random_seed.py

0.134
0.847
0.764
0.255
0.495

$ python random_seed.py

0.134
0.847
0.764
0.255
0.495
'''
