fo=open("a.txt",'a')

print "Current position",fo.tell()
fo.write("HI Its Sateesh")
print "Current position",fo.tell()
fo.close()