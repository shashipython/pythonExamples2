def fun(name,*marks):
    print name
	total=0
	print "===>",type(marks)
    for i in marks:
    	total+=i
    print "total:",total
	
fun("Shiva",34,50,67)