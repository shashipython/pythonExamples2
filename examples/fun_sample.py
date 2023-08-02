
'''
def fun_name():
    print "I am in fun"
	
fun_name()
'''
def fun_gen():
	print "I am her in fun"
	l=[]
	for i in range(10):
		l.append(i)
	return l
print "1st i am "	
p=fun_gen()
print "Gen Num:",p
	