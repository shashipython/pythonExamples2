import random

'''
choice(seq)
random()
randrange(start,end,step)
shuffle(list)
uniform(x,y)
seed(x)
'''

# This is for Choice
l=[23,34,35,56]
t=(10,23,20,50)
st="A String"
print "List:"
for i in range(5):
    print 'choice is:',random.choice(l)
print "Tuple:"
for i in range(5):
    print 'choice is:',random.choice(t)
    
print "Stringt:"
for i in range(5):
    print 'choice is:',random.choice(st)
    

print "RandRAnge:"
for i in range(5):
    print "==>",random.randrange(10,100,2)

print "Example on Random:"    
for i in range(6):
    p=random.random()
    print "Random Number:",p


l=[10,23,34,56]
for i in range(3):
    print "Befor Shuffle:",l
    random.shuffle(l)
    print "After Shufflue:",l    

print "Example for Range uniform"
for i in range(4):
    print "==>",random.uniform(30,50)


print "=>",random.random()
print "==>",random.seed(10000000)
print "=>",random.random()
