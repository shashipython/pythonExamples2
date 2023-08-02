def big_list(l):
    print "list",l
    big=l[0]
    for i in range(1,len(l)):
	    print i,"--",l[i]
	    if big<l[i]:
		    big=l[i]
    return big
	
l=[12,2,3,30,43,100,4]
big=big_list(l)
print "Biggest is ",big