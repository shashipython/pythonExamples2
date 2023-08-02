'''
randrange() supports a step argument, in addition to 
start and stop values, so it is fully equivalent to 
selecting a random value from range(start, stop, step). 
'''
import random

for i in xrange(3):
    print random.randrange(0, 101, 5)

'''
$ python random_randrange.py

50
55
45

'''