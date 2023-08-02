'''
The random() function returns the next random floating point 
value from the generated sequence range 0 <= n < 1.0.
'''

import random

for i in xrange(5):
    print '%04.3f' % random.random()
	

'''
$ python random_random.py

0.182
0.155
0.097
0.175
0.008

$ python random_random.py

0.851
0.607
0.700
0.922
0.496
'''
