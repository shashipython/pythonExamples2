'''
Reducing a List
The function reduce(func, seq) continually applies the function func() to the sequence seq. It returns a single value.

If seq = [ s1, s2, s3, ... , sn ], calling reduce(func, seq) works like this
func(s1,s2)
[ func(func(s1, s2),s3), ... , sn ]

'''

p=reduce(lambda x,y: x+y, [47,11,42,13])
print "Total:",p


f = lambda a,b: a if (a > b) else b
p=reduce(f, [47,11,42,102,13])
print "Biggest of all:",p

# calculetion sum of all the element in a list

l=reduce(lambda x, y: x+y, range(1,101))
print "Sum of all the element in the list:",l
