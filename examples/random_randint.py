'''
 randint() to generate integers directly is more convenient.
'''

import random

print '[1, 100]:'

for i in xrange(3):
    print random.randint(1, 100)

print
print '[-5, 5]:'
for i in xrange(3):
    print random.randint(-5, 5)

'''
$ python random_randint.py

[1, 100]:
3
47
72

[-5, 5]:
4
1
-3
'''